import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../services/api_service.dart';

class AuthProvider with ChangeNotifier {
  bool _isLoggedIn = false;
  bool _isLoading = false;
  String? _error;

  bool get isLoggedIn => _isLoggedIn;
  bool get isLoading => _isLoading;
  String? get error => _error;

  AuthProvider() {
    _checkAuth();
  }

  Future<void> _checkAuth() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');
    if (token != null) {
      _isLoggedIn = true;
      notifyListeners();
    }
  }

  Future<bool> login(String email, String password) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      final response = await ApiService.post('/usuarios/login', {
        'email': email,
        'senha': password,
      });

      if (response != null && response is Map && response.containsKey('access_token')) {
        final token = response['access_token'];
        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('access_token', token);
        _isLoggedIn = true;
        _isLoading = false;
        notifyListeners();
        return true;
      } else {
         _error = 'Resposta inválida do servidor';
      }
    } catch (e) {
      _error = e.toString().replaceAll('Exception: ', '');
    }
    
    _isLoading = false;
    notifyListeners();
    return false;
  }

  Future<bool> signup(String name, String email, String password) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await ApiService.post('/usuarios/', {
        'nome': name,
        'email': email,
        'senha': password,
      });

      // Auto login
      return await login(email, password);
    } catch (e) {
      _error = e.toString().replaceAll('Exception: ', '');
      _isLoading = false;
      notifyListeners();
      return false;
    }
  }

  Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('access_token');
    _isLoggedIn = false;
    notifyListeners();
  }
}
