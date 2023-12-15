import 'package:flutter/material.dart';
import 'package:theaterward/providers/theater_providers.dart';
import 'package:theaterward/models/theater_model.dart';
import 'package:theaterward/screens/theater_screen.dart';
import 'package:theaterward/providers/show_providers.dart';
import 'package:theaterward/models/show_model.dart';

String searchText = '';

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});

  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  List<Theater> theater = [];
  List<Show> show = [];
  bool isLoadingShow = true;
  bool isLoadingTheater = true;
  TheaterProviders theaterProvider = TheaterProviders();
  ShowProviders showProviders = ShowProviders();

  Future initTheater() async {
    theater = await theaterProvider.getTheaters();
  }

  Future initShow() async {
    show = await showProviders.getShows();
  }

  void theaterClick(BuildContext context, int index){
    int theaterNo = theater[index].no!;
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => TheaterScreen(no: theaterNo, type: 2,)),
    );
  }

  void showClick(BuildContext context, int index){
    int theaterNo = show[index].no!;
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => TheaterScreen(no: theaterNo, type: 1,)),
    );
  }

  @override
  void initState() {
    super.initState();
    initTheater().then((_) {
      setState(() {
        isLoadingTheater = false;
      });
    });
    initShow().then((_) {
      setState(() {
        isLoadingShow = false;
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
              SizedBox(width: 8,),
              Flexible(
                  flex: 1,
                  child: TextField(
                      decoration: InputDecoration(
                        contentPadding: EdgeInsets.symmetric(
                          vertical: 8,
                          horizontal: 16,
                        ),
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(
                            Radius.circular(8),
                          ),
                        ),
                        hintText: '검색 키워드를 입력해주세요',
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
                child: isLoadingShow ? const Center(child: CircularProgressIndicator(),) :
                ListView.builder(
                  itemCount: show.length,
                  itemBuilder: (BuildContext context, int index) {
                    if (searchText.isNotEmpty && !show[index].name!.toLowerCase().contains(searchText.toLowerCase())) {
                      return SizedBox.shrink();
                    }
                    else {
                      return Container(
                        padding: const EdgeInsets.all(10),
                        child: TextButton(
                            onPressed: () => showClick(context, index),
                            child: Text(show[index].name!)
                        ),
                      );
                    }
                  },
                )
            ),
            Tab(
              child: isLoadingTheater ? const Center(child: CircularProgressIndicator(),) :
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
