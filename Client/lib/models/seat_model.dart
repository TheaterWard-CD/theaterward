
class Seat {
  final int? theaterNo;
  final int? no;
  final int? row;
  final int? col;
  final int? floor;
  final String? coord;
  final String? keyword;

  Seat({
    required this.theaterNo,
    required this.no,
    required this.row,
    required this.col,
    required this.floor,
    required this.coord,
    required this.keyword,
  });

  factory Seat.fromJson(Map<String, dynamic> json) {
    return Seat(
      theaterNo: json['theaterNo'],
      no: json['seatNo'],
      row: json['seatRow'],
      col: json['seatCol'],
      floor: json['seatFloor'],
      coord: json['seatCoord'],
      keyword: json['seatKeyword'],
    );
  }
  Map<String, dynamic> toJson() => {
    'theaterNo': theaterNo,
    'seatNo': no,
    'seatRow': row,
    'seatFloor': floor,
    'seatCoord': coord,
    'seatKeyword': keyword,
  };
}