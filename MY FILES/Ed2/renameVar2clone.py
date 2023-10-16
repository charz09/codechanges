import os
import json
import spacy
import geopy.distance
from spacy.kb import KnowledgeBase
from geopy.geocoders import Nominatim

class Cap: #caption class

    cap = None
    top = None

    top_true_pos = 0
    top_false_pos = 0
    top_false_neg = 1

    loc_true_pos = 0
    loc_false_pos = 0
    loc_false_neg = 1

    def __init__(
            self,
            json_object): #class constructor
        self.caption = json_object["caption"] 
        self.ground_truth_toponym = json_object["ground truth toponym"]
        self.toponyms = []

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.caption)

        for ent in doc.ents:
            if ent.label_ in ["FAC", "GPE", "LOC"]:
                self.toponyms.append(Toponym(cap=self, string=ent.text))

        for loc in self.toponyms: 
            if loc.top == self.ground_truth_top:
                loc.top_true_pos = True
                self.top_true_pos = 1
                self.top_false_neg = 0
            else:
                loc.top_true_pos = False
                self.top_false_pos += 1

class Top: #toponym class
    top = None

    top_true_pos = None
    loc_true_pos = None

    def __init__(self, cap, string): #class constructor
        self.toponym = string
    


def get_captions(file_name): #retrieves captions from the json file 
    caps = []

    with open(file_name, "r") as file:
        data = json.load(file)

    for loc in data:
        caps.append(Caption(loc))

    return caps


def final(): #provides output
    captions = get_captions("json-capLatLong.json")
    caption_details = ""


    true_pos = 0
    false_pos = 0
    false_neg = 0

    for cap in captions:
        caption_details += "Caption: " + cap.caption + "\t""\t"

        if len(cap.toponyms) == 0:
            caption_details += "No entities detected."
        else:
            caption_details += "Entities: "
            for toponym in cap.toponyms:
                caption_details += toponym.toponym + ","

        true_pos += cap.top_true_pos
        false_pos += cap.top_false_pos
        false_neg += cap.top_false_neg

        caption_details += "\n"

    precision = true_pos / (true_pos + false_pos)
    recall = true_pos / len(captions)
    f1 = 2 * precision * recall / (precision + recall)
    
    print(caption_details)
    print("Number of true positives: " + str(true_pos))
    print("Number of false positives: " + str(false_pos))
    print("Number of false negatives: " + str(false_neg))
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("F1: " + str(f1))



final()