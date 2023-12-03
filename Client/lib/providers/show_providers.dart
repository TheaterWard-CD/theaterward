import 'dart:convert';

import 'package:theaterward/models/show_model.dart';
import 'package:http/http.dart' as http;

class ShowProviders{
  Uri request = Uri.parse("http://3.35.3.49/api/show");

  var jsonResponse;

  Future<List<Show>> getShows() async {
    List<Show> shows = [];
    final response = await http.get(request);
    shows = jsonDecode(utf8.decode(response.bodyBytes)).map<Show>( (t) {
      return Show.fromJson(t);
    }).toList();
    return shows;
  }

}