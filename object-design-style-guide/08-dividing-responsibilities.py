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
#   2023-03-30T20:13:22AEDT book uses name 'OrderForStockReport' (instead of 'OrderDetails')
#   }}}

#   Service objects may need to retrieve information and perform tasks.
#   However it is often beneficial to divide these responsibilities into separate objects.


#   8.1) Separate write models from read models
#   Provide a separate read-only <(view into?)> objects for clients who do not need to modify them

#   Example: separate 'Order' into write/read-model classes
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
    
    class StockReportController:
        def __init__(self, repository: OrderRepository):
            self.repository = repository
        def execute(self):
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
    
    def test_StockReportController():
        repo = OrderRepository()
        recieve = RecieveItems(repo)
        reporter = StockReportController(repo)
        repo.save(Order(1, 53, 7))
        repo.save(Order(2, 9, 4))
        repo.save(Order(3, 53, 5))
        repo.save(Order(4, 9, 23))
        report = reporter.execute()
        assert report == '{}'
        recieve.recieveItems(1)
        recieve.recieveItems(2)
        recieve.recieveItems(3)
        report = reporter.execute()
        assert report == '{53: 12, 9: 4}'
    
    test_StockReportController()

_8_1()


#   8.2) Create read models that are specific for their use cases
#   <(an improved design to 8.1 could be to add a 'getStockReport()' method to 'OrderRepository')>
#   contention: 'OrderForStockReport' is an acceptable name for a read-model object specifically for 'StockReportController'
#   <>

def _8_2():
    ...


#   8.3) Create read models directly from their data source
#   <>

