places = {
    "Meenakshi Temple": {
        "category": "Temple",
        "visit_time": 2,
        "cost": 0,
        "rating": 4.8,
        "nearby": {
            "Thirumalai Nayakkar Palace": 2,
            "Gandhi Memorial Museum": 4,
            "Vandiyur Mariamman Teppakulam": 4
        }
    },

    "Thirumalai Nayakkar Palace": {
        "category": "Historical",
        "visit_time": 1.5,
        "cost": 50,
        "rating": 4.5,
        "nearby": {
            "Meenakshi Temple": 2,
            "Gandhi Memorial Museum": 3,
            "Vandiyur Mariamman Teppakulam": 5
        }
    },

    "Gandhi Memorial Museum": {
        "category": "Museum",
        "visit_time": 1.5,
        "cost": 20,
        "rating": 4.4,
        "nearby": {
            "Meenakshi Temple": 4,
            "Thirumalai Nayakkar Palace": 3,
            "Vandiyur Mariamman Teppakulam": 4,
            "Alagar Koyil": 21
        }
    },

    "Vandiyur Mariamman Teppakulam": {
        "category": "Nature",
        "visit_time": 1,
        "cost": 0,
        "rating": 4.3,
        "nearby": {
            "Meenakshi Temple": 4,
            "Thirumalai Nayakkar Palace": 5,
            "Gandhi Memorial Museum": 4
        }
    },

    "Alagar Koyil": {
        "category": "Temple",
        "visit_time": 2,
        "cost": 0,
        "rating": 4.7,
        "nearby": {
            "Gandhi Memorial Museum": 21,
            "Meenakshi Temple": 22
        }
    }
}
heuristics = {
    "Meenakshi Temple": {
        "Gandhi Memorial Museum": 4,
        "Thirumalai Nayakkar Palace": 2,
        "Vandiyur Mariamman Teppakulam": 4,
        "Alagar Koyil": 22
    },

    "Thirumalai Nayakkar Palace": {
        "Gandhi Memorial Museum": 3,
        "Meenakshi Temple": 2,
        "Vandiyur Mariamman Teppakulam": 5,
        "Alagar Koyil": 21
    },

    "Gandhi Memorial Museum": {
        "Meenakshi Temple": 4,
        "Thirumalai Nayakkar Palace": 3,
        "Vandiyur Mariamman Teppakulam": 4,
        "Alagar Koyil": 21
    },

    "Vandiyur Mariamman Teppakulam": {
        "Meenakshi Temple": 4,
        "Thirumalai Nayakkar Palace": 5,
        "Gandhi Memorial Museum": 4,
        "Alagar Koyil": 22
    },

    "Alagar Koyil": {
        "Meenakshi Temple": 22,
        "Thirumalai Nayakkar Palace": 21,
        "Gandhi Memorial Museum": 21,
        "Vandiyur Mariamman Teppakulam": 25
    }
}