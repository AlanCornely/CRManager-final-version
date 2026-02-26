import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../models/product.dart';
import '../models/client.dart';

class InventoryProvider with ChangeNotifier {
  List<Product> _products = [];
  List<Client> _clients = [];
  bool _isLoading = false;
  String? _error;

  List<Product> get products => _products;
  List<Client> get clients => _clients;
  bool get isLoading => _isLoading;
  String? get error => _error;

  // Stats
  double get totalStockValue => _products.fold(0, (sum, item) => sum + (item.quantity * item.salePrice));
  int get totalItems => _products.fold(0, (sum, item) => sum + item.quantity);
  int get lowStockCount => _products.where((i) => i.quantity < 5).length;

  Future<void> fetchProducts() async {
    _isLoading = true;
    notifyListeners();
    try {
      final response = await ApiService.get('/produtos/');
      if (response != null && response is List) {
        _products = response.map((e) => Product.fromJson(e)).toList();
      }
    } catch (e) {
      _error = e.toString();
    }
    _isLoading = false;
    notifyListeners();
  }

  Future<void> fetchClients() async {
    // Mocked because backend/api/v1/clientes.py is empty
    await Future.delayed(const Duration(milliseconds: 500));
    _clients = [
      Client(id: 1, name: 'Empresa XYZ Ltda', cpf: '00.000.000/0001-00', city: 'São Paulo', state: 'SP', registrationDate: '2024-01-15'),
      Client(id: 2, name: 'João Silva', cpf: '123.456.789-00', city: 'Rio de Janeiro', state: 'RJ', registrationDate: '2024-01-20'),
    ];
    notifyListeners();
  }

  Future<void> addProduct(Map<String, dynamic> productData) async {
    try {
      await ApiService.post('/produtos/', productData);
      await fetchProducts();
    } catch (e) {
      rethrow;
    }
  }
  
  // Placeholder for sale logic (decrement stock)
  // In real backend, safe to assume sale endpoint would handle this.
  // Since we mock sales, we might need to decrement locally or via item update.
  Future<void> decrementStock(int productId, int quantity) async {
     // TODO: Implement update via API or logic
  }
}
