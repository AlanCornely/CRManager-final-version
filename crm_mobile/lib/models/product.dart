class Product {
  final int id;
  final String name;
  final String? description;
  final String? sku;
  final String? barcode;
  final int quantity;
  final double costPrice;
  final double salePrice;
  final String? categoryName;
  final String? providerName;
  final String? location;

  Product({
    required this.id,
    required this.name,
    this.description,
    this.sku,
    this.barcode,
    required this.quantity,
    required this.costPrice,
    required this.salePrice,
    this.categoryName,
    this.providerName,
    this.location,
  });

  factory Product.fromJson(Map<String, dynamic> json) {
    return Product(
      id: json['id_produto'],
      name: json['nome'],
      description: json['descricao'],
      sku: json['sku'],
      barcode: json['codigo_barras'],
      quantity: json['quantidade_atual'] ?? 0,
      costPrice: (json['preco_custo'] ?? 0).toDouble(),
      salePrice: (json['preco_venda'] ?? 0).toDouble(),
      categoryName: json['categoria_nome'],
      providerName: json['fornecedor_nome'],
      location: json['localizacao'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id_produto': id,
      'nome': name,
      'descricao': description,
      'sku': sku,
      'codigo_barras': barcode,
      'quantidade_atual': quantity,
      'preco_custo': costPrice,
      'preco_venda': salePrice,
      'categoria_nome': categoryName,
      'fornecedor_nome': providerName,
      'localizacao': location,
    };
  }
}
