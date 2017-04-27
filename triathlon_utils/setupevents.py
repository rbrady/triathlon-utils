#!/usr/bin/env python
import datetime
import time


def get_base_time(scores):
    """Calculates base time
    
    The top 5 times in the category will be converted to seconds and
    used to create an average time that all times in the category will
    be divided into.
    """
    return sum([get_seconds(score) for score in scores]) / len(scores)


def get_raw_score(basetime, race_result):
    """Calculates raw score for a given participant race result
    
    All participants' times in that category will be converted to
    seconds and divided into the categories "Base" time to create
    "Raw" scores for that category.
    """
    return basetime / get_seconds(race_result)


def get_seconds(race_result):
    t1 = time.strptime(race_result, "%H:%M:%S")
    d = datetime.timedelta(
        hours=t1.tm_hour, minutes=t1.tm_min, seconds=t1.tm_sec)
    return d.total_seconds()


def get_score(race_result, group_results, event_weight):
	basetime = get_base_time(group_results[:5])
	raw = get_raw_score(basetime, race_result)
	return raw * event_weight * 10000.0
    

