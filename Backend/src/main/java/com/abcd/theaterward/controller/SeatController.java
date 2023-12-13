package com.abcd.theaterward.controller;

import com.abcd.theaterward.domain.GradeAndPrice;
import com.abcd.theaterward.domain.Seat;
import com.abcd.theaterward.domain.SeatShows;
import com.abcd.theaterward.service.SeatService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
public class SeatController {
    private final SeatService seatService;

    public SeatController(SeatService seatService) {
        this.seatService = seatService;
    }

    @GetMapping("/seat/{theaterno}")
    public List<Seat> findSeats(@PathVariable int theaterno) {
        return seatService.findSeats(theaterno);
    }




    @GetMapping("/seat")
    public Object getGradeAndPrice(@RequestBody ByShowRequest byShowRequest) {
        if(byShowRequest.getType() == 1) {
            //Search By Show (Type : 1)
            return seatService.findGradeAndPriceByTheaterNoAndShowNameAndShowYear
                    (byShowRequest.getTheaterNo(),
                            byShowRequest.getShowsName(),
                            byShowRequest.getShowsYear(),
                            byShowRequest.getSeatNo());
        }
        else {
            //Search By Theater (Type : 2)
            return seatService.findRangeByTheaterNo
                    (byShowRequest.getTheaterNo(),
                            byShowRequest.getSeatNo());
        }
    }
//    public List<SeatShows> getGradeAndPrice(@RequestBody ByShowRequest byShowRequest) {
//        return seatService.findGradeAndPriceByTheaterNoAndShowNameAndShowYear(
//                byShowRequest.getTheaterNo(),
//                byShowRequest.getShowsName(),
//                byShowRequest.getShowsYear(),
//                byShowRequest.getSeatNo()
//        );
//    }

    public static class ByShowRequest {
        private int type;
        private String showsName;
        private int showsYear;
        private int theaterNo;
        private int seatNo;

        public String getShowsName() {
            return showsName;
        }

        public int getShowsYear() {
            return showsYear;
        }

        public int getTheaterNo() {
            return theaterNo;
        }

        public int getSeatNo() {
            return seatNo;
        }

        public int getType() {
            return type;
        }

        public ByShowRequest() {
        }
    }
}
