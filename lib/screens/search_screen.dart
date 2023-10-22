import 'package:flutter/material.dart';
import 'package:theaterward/providers/theater_providers.dart';
import 'package:theaterward/models/theater_model.dart';
import 'package:theaterward/screens/theater_screen.dart';

String searchText = '';

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});

  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  List<Theater> theater = [];
  bool isLoading = true;
  TheaterProviders theaterProvider = TheaterProviders();

  Future initTheater() async {
    theater = await theaterProvider.getTheaters();
  }

  void theaterClick(BuildContext context, int index){
    int theaterNo = theater[index].no!;
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => TheaterScreen(no: theaterNo)),
    );
  }

  @override
  void initState() {
    super.initState();
    initTheater().then((_) {
      setState(() {
        isLoading = false;
      });
    });
  }
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.white,
          title: Row(
            mainAxisAlignment: MainAxisAlignment.start,
            mainAxisSize: MainAxisSize.max,
            children: [
              Icon(Icons.search),
              Flexible(
                  flex: 1,
                  child: TextField(
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                    ),
                    onChanged: (value){
                      setState(() {
                        searchText = value;
                      });
                    },
                  )
              ),
            ],
          ),
          bottom: const TabBar(
            tabs: <Widget>[
              Tab(child: Text('Show'),),
              Tab(child: Text('Theater'),),
            ],
          ),
        ),
        body: TabBarView(
          children: <Widget>[
            Tab(
              child: ListView(

              ),
            ),
            Tab(
              child: isLoading ? const Center(child: CircularProgressIndicator(),) :
              ListView.builder(
                itemCount: theater.length,
                itemBuilder: (BuildContext context, int index) {
                  if (searchText.isNotEmpty && !theater[index].name!.toLowerCase().contains(searchText.toLowerCase())) {
                    return SizedBox.shrink();
                  }
                  else {
                    return Container(
                      padding: const EdgeInsets.all(10),
                      child: TextButton(
                          onPressed: () => theaterClick(context, index),
                          child: Text(theater[index].name!)
                      ),
                    );
                  }
                },
              )
            ),
          ],
        )

      ),
    );
  }
}
