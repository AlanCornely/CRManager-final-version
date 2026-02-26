import 'package:flutter/material.dart';

class Sale {
  final int id;
  final String clientName;
  final String itemName;
  final int quantity;
  final double total;
  final String paymentMethod;
  final String date;

  Sale({
    required this.id,
    required this.clientName,
    required this.itemName,
    required this.quantity,
    required this.total,
    required this.paymentMethod,
    required this.date,
  });
}

class SalesProvider with ChangeNotifier {
  List<Sale> _sales = [];
  
  List<Sale> get sales => _sales;
  List<Sale> get recentSales => _sales.reversed.take(5).toList();
  
  double get totalSalesValue => _sales.fold(0, (sum, item) => sum + item.total);
  int get salesTodayCount => _sales.length; // Mock, assumes all sales are today

  void addSale(Sale sale) {
    _sales.add(sale);
    notifyListeners();
  }
}
