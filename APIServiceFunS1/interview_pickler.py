import pickle 
# a standard python library
# pickle (AKA object serialization): writing a binary representation of an object to a file
# unpickle (AKA object de-serialization): read a binary representation of an object from a file
# to load a python object in to memory


# for the project... imagine this is a MyRandomForestClassifier
# for PA6... imagine this is a MyDecisionTreeClassifier
# both of which were just trained with fit()
header = ["level", "lang", "tweets", "phd"]

interview_tree = \
["Attribute", "level", 
    ["Value", "Senior", 
        ["Attribute", "tweets", 
            ["Value", "yes", 
                ["Leaf", "True", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "False", 3, 5]
            ]
        ]
    ],
    ["Value", "Mid", 
        ["Leaf", "True", 4, 14]
    ],
    ["Value", "Junior", 
        ["Attribute", "phd", 
            ["Value", "yes", 
                ["Leaf", "False", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "True", 3, 5]
            ]
        ]
    ]
]

# pickle (save to file) header and interview tree as one object
packaged_object = [header, interview_tree]
outfile = open("tree.p", "wb")
pickle.dump(packaged_object, outfile)
outfile.close()
