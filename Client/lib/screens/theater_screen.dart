import 'package:flutter/material.dart';
import 'package:theaterward/providers/seat_providers.dart';
import 'package:theaterward/models/seat_model.dart';
import 'package:theaterward/screens/seat_screen.dart';
import 'package:book_my_seat/book_my_seat.dart';

class TheaterScreen extends StatefulWidget {
  final int no;
  final int type;
  SeatProviders seatProviders = SeatProviders(theaterNo: 1);

  TheaterScreen({Key? key, required this.no, required this.type}) {
    key = super.key;
    seatProviders = SeatProviders(theaterNo: no);
  }

  @override
  State<TheaterScreen> createState() => _TheaterScreenState();
}

class _TheaterScreenState extends State<TheaterScreen> {
  List<Seat> seat = [];
  bool isLoading = true;

  Future initSeat() async {
    seat = await widget.seatProviders.getSeats();
  }

  @override
  void initState() {
    super.initState();
    initSeat().then((_) {
      setState(() {
        isLoading = false;
      });
    });
  }

  void seatClick(BuildContext context, int index){
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => SeatScreen(seat: seat[index], type: widget.type,)),
    );
  }

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Theater Screen"),
      ),
      body: isLoading ? const Center(child: CircularProgressIndicator(),) :
          // SeatLayoutWidget(
          //     stateModel: stateModel,
          //     onSeatStateChanged: onSeatStateChanged
          // )
      GridView.builder(
          gridDelegate:SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 8, //1 개의 행에 보여줄 item 개수
            childAspectRatio: 1 / 1, //item 의 가로 1, 세로 1 의 비율
            mainAxisSpacing: 3, //수평 Padding
            crossAxisSpacing: 3, //수직 Padding
          ),
        itemCount: seat.length,
        itemBuilder: (BuildContext context, int index) {
          return Container(
            //padding: const EdgeInsets.all(10),
            child: TextButton(
                onPressed: () => seatClick(context, index),
                child: Text('${seat[index].no!}')
            ),
          );
        }
      )

    );
  }
}