import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  // Use 10.0.2.2 for Android emulator to access localhost of the host machine.
  // Use localhost for iOS simulator or web.
  // We'll try to detect or just use a const that can be swapped.
  static const String baseUrl = 'http://10.0.2.2:8000/api/v1'; 
  
  static Future<Map<String, String>> getHeaders() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');
    return {
      'Content-Type': 'application/json',
      if (token != null) 'Authorization': 'Bearer $token',
    };
  }

  static Future<dynamic> post(String endpoint, Map<String, dynamic> data) async {
    final url = Uri.parse('$baseUrl$endpoint');
    final headers = await getHeaders();
    
    try {
      final response = await http.post(
        url,
        headers: headers,
        body: jsonEncode(data),
      );
      
      return _handleResponse(response);
    } catch (e) {
      throw Exception('Erro de conexão: $e');
    }
  }

  static Future<dynamic> get(String endpoint) async {
    final url = Uri.parse('$baseUrl$endpoint');
    final headers = await getHeaders();
    
    try {
      final response = await http.get(url, headers: headers);
      return _handleResponse(response);
    } catch (e) {
      throw Exception('Erro de conexão: $e');
    }
  }

  static dynamic _handleResponse(http.Response response) {
    if (response.statusCode >= 200 && response.statusCode < 300) {
      // Decode only if body is not empty
      if (response.body.isNotEmpty) {
        return jsonDecode(response.body);
      }
      return null;
    } else {
      // Try to parse error message
      String message = 'Erro desconhecido (${response.statusCode})';
      try {
        final errorBody = jsonDecode(response.body);
        if (errorBody is Map && errorBody.containsKey('detail')) {
          message = errorBody['detail'];
        }
      } catch (_) {}
      throw Exception(message);
    }
  }
}
