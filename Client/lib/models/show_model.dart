
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
      name: json['showName'],
      year: json['showYear'],
      no: json['theaterNo'],
    );
  }
  Map<String, dynamic> toJson() => {
    'showName': name,
    'showYear': year,
    'theaterNo': no,
  };
}