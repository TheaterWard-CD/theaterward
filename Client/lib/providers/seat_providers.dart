import 'dart:convert';

import 'package:theaterward/models/seat_model.dart';
import 'package:http/http.dart' as http;

class SeatProviders{
  final int? theaterNo;
  Uri request = Uri.parse("http://3.35.3.49/api/seat/1");

  SeatProviders({required this.theaterNo}) {
    this.request = Uri.parse("http://3.35.3.49/api/seat/"+theaterNo.toString());
  }

  var jsonResponse;

  Future<List<Seat>> getSeats() async {
    List<Seat> seats = [];
    final response = await http.get(request);
    seats = jsonDecode(utf8.decode(response.bodyBytes)).map<Seat>( (t) {
      return Seat.fromJson(t);
    }).toList();
    return seats;
  }

}