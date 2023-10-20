import 'dart:convert';

import 'package:theaterward/models/theater_model.dart';
import 'package:http/http.dart' as http;

class TheaterProviders{
  Uri request = Uri.parse("http://3.35.3.49/api/theater");

  var jsonResponse;

  Future<List<Theater>> getTheaters() async {
    List<Theater> theaters = [];
    final response = await http.get(request);
    theaters = jsonDecode(utf8.decode(response.bodyBytes)).map<Theater>( (t) {
      return Theater.fromJson(t);
    }).toList();
    return theaters;
  }

}