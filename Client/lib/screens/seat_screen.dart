import 'package:flutter/material.dart';
import 'package:theaterward/models/seat_model.dart';
import 'package:theaterward/widgets/view_widget.dart';
import 'package:theaterward/models/review_model.dart';
import 'package:theaterward/providers/review_providers.dart';

class SeatScreen extends StatefulWidget {
  int seatNo = 0;
  SeatScreen({super.key, required Seat seat, required int type}) {
    seatNo = seat.no!;
  }

  @override
  State<SeatScreen> createState() => _SeatScreenState();
}

class _SeatScreenState extends State<SeatScreen> {
  List<Review> review = [];
  bool isLoading = true;
  int seatNo = 0;
  ReviewProviders reviewProviders = ReviewProviders();

  Future initReview() async {
    review = await reviewProviders.getReview();
  }

  @override
  void initState() {
    super.initState();
    initReview().then((_) {
      setState(() {
        isLoading = false;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(

      ),
      body: Column(
        children: [
          Expanded(
            child: Character(seatNo: widget.seatNo,),
          ),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          children: [
            //UserAccountsDrawerHeader(accountName: Text('User'), accountEmail: Text('user@gmail.com')),
            ListTile(
              leading: Icon(Icons.home),
              title: Text('Home'),
              onTap: () {
                Navigator.of(context).popUntil((route) => route.isFirst);
              },
              trailing: Icon(Icons.navigate_next),
            ),
            ListTile(
              leading: Icon(Icons.settings),
              title: Text('리뷰'),
              onTap: () {
                showModalBottomSheet(
                  context: context,
                  builder: (context) {
                    return Expanded(
                      child: isLoading ? const Center(child: CircularProgressIndicator(),) :
                      ListView.builder(
                        itemCount: review.length,
                        itemBuilder: (BuildContext context, int idx) {
                          return Text(review[idx].reviewContent!);
                        },
                      ),
                    );
                  }
                );
              },
              trailing: Icon(Icons.navigate_next),
            ),
          ],
        ),
      ),
    );
  }
}
