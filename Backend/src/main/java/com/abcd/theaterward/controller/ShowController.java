package com.abcd.theaterward.controller;

import com.abcd.theaterward.domain.Show;
import com.abcd.theaterward.service.ShowService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api")
public class ShowController {
    private final ShowService showService;

    public ShowController(ShowService showService) {
        this.showService = showService;
    }

    @GetMapping("/shows")
    public List<Show> findShows() {
        return showService.findShows();
    }
}
