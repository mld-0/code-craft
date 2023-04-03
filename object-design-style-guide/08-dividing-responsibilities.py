#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from __future__ import annotations
import sys
import os
import unittest
from typing import List
from dataclasses import dataclass
#   Notes:
#   {{{
#   2023-03-30T20:03:44AEDT 'Order' / 'OrderDetails' seems convoluted for minimal benefit -> (better example for "Separate write models from read models"
#   2023-03-30T20:13:22AEDT book uses name 'OrderForStockReport' (instead of 'OrderDetails') [...] (I mean, if going that route, call it 'Order_ForStockReport'?)
#   2023-04-03T20:44:46AEST 8.4 example -> 'RecieveItems' is the place to call 'StockTable.recieve()' (not inside 'Order.markAsRecieved()'</elsewhere>?)
#   2023-04-03T20:46:27AEST *both* examples are poor design(?)
#   2023-04-03T20:49:57AEST calculating quantity in stock by reading existing database tables is almost certainly the better decision than using domain-events to create read-model(?)
#   }}}

#   Service objects may need to retrieve information and perform tasks.
#   However it is often beneficial to divide these responsibilities into separate objects.


#   8.1) Separate write models from read models
#   Provide a separate read-only <(view into?)> objects for clients who do not need to modify them

#   Example: create read-model objects from write-model objects to generate stock report
#   {{{
def _8_1():
    class Order:
        def __init__(self, purchaseOrderId: int, productId: int, orderQuantity: int) -> Order:
            self._purchaseOrderId = purchaseOrderId
            self._productId = productId
            self._orderQuantity = orderQuantity
            self._wasRecieved = False
        def purchaseOrderId(self) -> int:
            return self._purchaseOrderId
        def markAsRecieved(self):
            if self._wasRecieved:
                raise Exception(f"order=({self._purchaseOrderId}) already recieved")
            self._wasRecieved = True
        def toOrderDetails(self) -> OrderDetails:
            return OrderDetails(self._productId, self._orderQuantity, self._wasRecieved)

    class OrderDetails:
        def __init__(self, productId: int, orderQuantity: int, wasRecieved: bool):
            self._productId = productId
            self._orderQuantity = orderQuantity
            self._wasRecieved = wasRecieved
        def productId(self) -> int:
            return self._productId
        def orderQuantity(self) -> int:
            return self._orderQuantity
        def wasRecieved(self) -> bool:
            return self._wasRecieved

    class OrderRepository:
        def __init__(self):
            self.orders = dict()
        def save(self, purchaseOrder: Order):
            if purchaseOrder.purchaseOrderId() in self.orders.keys():
                raise Exception("purchaseOrderId=({purchaseOrder.purchaseOrderId}) already recorded")
            self.orders[purchaseOrder.purchaseOrderId()] = purchaseOrder
        def getById(self, purchaseOrderId: int) -> Order:
            return self.orders[purchaseOrderId]
        def getAll(self) -> List[Order]:
            return list(self.orders.values())

    class RecieveItems:
        def __init__(self, repository: OrderRepository):
            self.repository = repository
        def recieveItems(self, purchaseOrderId: int):
            purchaseOrder = self.repository.getById(purchaseOrderId)
            purchaseOrder.markAsRecieved()

    class StockReportCreator:
        def __init__(self, repository: OrderRepository):
            self.repository = repository
        def execute(self) -> str:
            allOrders = self.repository.getAll()
            toOrderDetails = [ x.toOrderDetails() for x in allOrders ]
            stockReport = dict()
            for purchaseOrder in toOrderDetails:
                if not purchaseOrder.wasRecieved():
                    continue
                if not purchaseOrder.productId() in stockReport.keys():
                    stockReport[purchaseOrder.productId()] = 0
                stockReport[purchaseOrder.productId()] += purchaseOrder.orderQuantity()
            return str(stockReport)

    def test_StockReportCreator():
        repo = OrderRepository()
        repo.save(Order(1, 53, 7))
        repo.save(Order(2, 9, 4))
        repo.save(Order(3, 53, 5))
        repo.save(Order(4, 9, 23))
        reporter = StockReportCreator(repo)
        report = reporter.execute()
        assert report == '{}'
        recieve = RecieveItems(repo)
        recieve.recieveItems(1)
        recieve.recieveItems(2)
        recieve.recieveItems(3)
        report = reporter.execute()
        assert report == '{53: 12, 9: 4}'

    test_StockReportCreator()

_8_1()
#   }}}


#   8.2) Create read models that are specific for their use cases
#   <(an improved design to 8.1 could be to add a 'getStockReport()' method to 'OrderRepository')>
#   contention: 'OrderForStockReport' is an acceptable name for a read-model object specifically for 'StockReportCreator'
#   contention: consider creating different read-models for different use cases


#   8.3) Create read models directly from their data source
#   Instead of using our dict of 'OrderDetails' objects to create the stock report, read the data from the database directly


#   8.4) Build read models from domain events
#   Querying the orders table in the database to calculate stock reports is likely to be slow.
#   Instead, create a new table quantities_in_stock, and have an Event dispatcher/handler update this table whenever 'recieveItems()' is called.

#   Example: use domain events to build read-model for stock report
#   {{{
def _8_4():
    class Order:
        def __init__(self, purchaseOrderId: int, productId: int, orderQuantity: int) -> Order:
            self._purchaseOrderId = purchaseOrderId
            self._productId = productId
            self._orderQuantity = orderQuantity
            self._wasRecieved = False
        def purchaseOrderId(self) -> int:
            return self._purchaseOrderId
        def productId(self) -> int:
            return self._productId
        def orderQuantity(self) -> int:
            return self._orderQuantity
        def wasRecieved(self) -> bool:
            return self._wasRecieved
        def markAsRecieved(self):
            if self._wasRecieved:
                raise Exception(f"order=({self._purchaseOrderId}) already recieved")
            self._wasRecieved = True

    class OrderRepository:
        def __init__(self):
            self.orders = dict()
        def save(self, purchaseOrder: Order):
            if purchaseOrder.purchaseOrderId() in self.orders.keys():
                raise Exception("purchaseOrderId=({purchaseOrder.purchaseOrderId}) already recorded")
            self.orders[purchaseOrder.purchaseOrderId()] = purchaseOrder
        def getById(self, purchaseOrderId: int) -> Order:
            return self.orders[purchaseOrderId]
        def getAll(self) -> List[Order]:
            return list(self.orders.values())

    class RecieveItems:
        def __init__(self, repository: OrderRepository):
            self.repository = repository
        def recieveItems(self, purchaseOrderId: int):
            purchaseOrder = self.repository.getById(purchaseOrderId)
            purchaseOrder.markAsRecieved()
            StockTable.recieve(purchaseOrder)

    class StockTable:
        table = dict()
        def recieve(purchaseOrder: Order):
            assert purchaseOrder.wasRecieved()
            if not purchaseOrder.productId() in StockTable.table.keys():
                StockTable.table[purchaseOrder.productId()] = 0
            StockTable.table[purchaseOrder.productId()] += purchaseOrder.orderQuantity()

    class StockReportCreator:
        def __init__(self, repository: OrderRepository):
            self.repository = repository
        def execute(self) -> str:
            return str(StockTable.table)

    def test_StockReportCreator():
        repo = OrderRepository()
        repo.save(Order(1, 53, 7))
        repo.save(Order(2, 9, 4))
        repo.save(Order(3, 53, 5))
        repo.save(Order(4, 9, 23))
        reporter = StockReportCreator(repo)
        report = reporter.execute()
        assert report == '{}'
        recieve = RecieveItems(repo)
        recieve.recieveItems(1)
        recieve.recieveItems(2)
        recieve.recieveItems(3)
        report = reporter.execute()
        assert report == '{53: 12, 9: 4}'

    test_StockReportCreator()

_8_4()
#   }}}


#   Summary:
#   For domain objects, separate read models from write models. Clients that only need to retrieve data should use a read model object.
#   A read model can be created directly from a write model, but it can be more efficient to use the data source used by the write model instead. If that is too expensive, consider creating a new data source that is updated by domain events.

