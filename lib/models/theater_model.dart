
class Theater {
  final int? no;
  final String? name;
  final String? wall;
  final String obj;
  final String? stage;

  Theater({
    required this.no,
    required this.name,
    required this.wall,
    required this.obj,
    required this.stage,
  });

  factory Theater.fromJson(Map<String, dynamic> json) {
    return Theater(
      no: json['theaterNo'],
      name: json['theaterName'],
      wall: json['theaterWall'],
      obj: json['theaterObj'],
      stage: json['theaterStage'],
    );
  }
  Map<String, dynamic> toJson() => {
    'theaterNo': no,
    'theaterName': name,
    'theaterWall': wall,
    'theaterObj': obj,
    'theaterStage': stage,
  };
}