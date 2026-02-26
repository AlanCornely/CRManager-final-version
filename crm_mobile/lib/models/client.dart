class Client {
  final int id;
  final String name;
  final String? cpf;
  final String? address;
  final String? city;
  final String? state;
  final String? zipCode;
  final String? registrationDate;

  Client({
    required this.id,
    required this.name,
    this.cpf,
    this.address,
    this.city,
    this.state,
    this.zipCode,
    this.registrationDate,
  });

  factory Client.fromJson(Map<String, dynamic> json) {
    return Client(
      id: json['id_cliente'],
      name: json['nome'],
      cpf: json['cpf'],
      address: json['endereco'],
      city: json['cidade'],
      state: json['estado'],
      zipCode: json['cep'],
      registrationDate: json['data_cadastro'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id_cliente': id,
      'nome': name,
      'cpf': cpf,
      'endereco': address,
      'cidade': city,
      'estado': state,
      'cep': zipCode,
      'data_cadastro': registrationDate,
    };
  }
}
