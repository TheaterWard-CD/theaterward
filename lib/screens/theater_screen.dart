import 'package:flutter/material.dart';
import 'package:theaterward/providers/seat_providers.dart';
import 'package:theaterward/models/seat_model.dart';

class TheaterScreen extends StatelessWidget {
  final int no;
  SeatProviders seatProviders = SeatProviders(theaterNo: 1);

  TheaterScreen({Key? key, required this.no}) {
    key = super.key;
    seatProviders = SeatProviders(theaterNo: no);
  }

  List<Seat> seat = [];

  Future initSeat() async {
    seat = await seatProviders.getSeats();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Theater Screen"),
      ),
      body: Center(
        child: Text("Theater No: $no"),
      ),
    );
  }
}