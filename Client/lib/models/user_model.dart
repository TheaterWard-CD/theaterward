
class User {
  final String? id;
  final String? pw;
  final String? name;
  final String? email;
  final String? gender;
  final int? tall;

  User({
    required this.id,
    required this.pw,
    required this.name,
    required this.email,
    required this.gender,
    required this.tall
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['user_id'],
      pw: json['user_pw'],
      name: json['user_name'],
      email: json['user_email'],
      gender: json['user_gender'],
      tall: json['user_tall'],
    );
  }
  Map<String, dynamic> toJson() => {
    'user_id': id,
    'user_pw': pw,
    'user_name': name,
    'user_email': email,
    'user_gender': gender,
    'user_tall': tall,
  };
}