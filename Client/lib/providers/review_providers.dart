import 'dart:convert';

import 'package:theaterward/models/review_model.dart';
import 'package:http/http.dart' as http;

class ReviewProviders{
  Uri request = Uri.parse("http://3.35.3.49/api/review");

  var jsonResponse;

  Future<List<Review>> getReview() async {
    List<Review> reviews = [];
    final response = await http.get(request);
    print('print post review${jsonDecode(utf8.decode(response.bodyBytes))}');
    reviews = jsonDecode(utf8.decode(response.bodyBytes)).map<Review>( (t) {
      return Review.fromJson(t);
    }).toList();
    return reviews;
  }
}