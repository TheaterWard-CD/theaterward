
class Show {
  final String? name;
  final int? year;
  final int? no;

  Show({
    required this.name,
    required this.year,
    required this.no,
  });

  factory Show.fromJson(Map<String, dynamic> json) {
    return Show(
      name: json['show_name'],
      year: json['show_year'],
      no: json['show_no'],
    );
  }
  Map<String, dynamic> toJson() => {
    'show_name': name,
    'show_year': year,
    'show_no': no,
  };
}