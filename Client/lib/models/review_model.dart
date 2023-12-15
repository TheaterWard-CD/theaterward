class Review {
  final String? userId;
  final int? reviewScore;
  final String? reviewContent;
  final int? theaterNo;
  final int? seatNo;
  final String? showName;
  final int? showYear;

  Review({
    required this.userId,
    required this.reviewScore,
    required this.reviewContent,
    required this.theaterNo,
    required this.seatNo,
    required this.showName,
    required this.showYear,
  });

  factory Review.fromJson(Map<String, dynamic> json) {
    return Review(
      userId: json['userId'],
      reviewScore: json['reviewScore'],
      reviewContent: json['reviewContent'],
      theaterNo: json['theaterNo'],
      seatNo: json['seatNo'],
      showName: json['showName'],
      showYear: json['showYear'],
    );
  }
  Map<String, dynamic> toJson() => {
    'userId': userId,
    'reviewScore': reviewScore,
    'reviewContent': reviewContent,
    'theaterNo': theaterNo,
    'seatNo': seatNo,
    'showName': showName,
    'showYear': showYear,
  };
}