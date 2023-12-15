package com.abcd.theaterward.controller;


import com.abcd.theaterward.domain.Member;
import com.abcd.theaterward.domain.Theater;
import com.abcd.theaterward.domain.TheaterP;
import com.abcd.theaterward.service.TheaterService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api")
public class TheaterController {

    private final TheaterService theaterService;

    public List<TheaterP> parsed = new ArrayList<>();

    public TheaterController(TheaterService theaterService) {
        this.theaterService = theaterService;
    }

    @GetMapping("/theater")
    public List<TheaterP> findTheaters() {
        List<Theater> TheaterNP = theaterService.findTheaters();
        List<TheaterP> TheaterP = new ArrayList<>();
        for(Theater theater : TheaterNP) {
            TheaterP theaterP = new TheaterP(theater);
            TheaterP.add(theaterP);
        }
        return TheaterP;
        //return theaterService.findTheaters();
    }
}
