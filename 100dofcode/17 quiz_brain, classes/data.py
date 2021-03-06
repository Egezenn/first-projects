question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_data_expanded = [{"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                           "question": "Igneous rocks are formed by excessive heat and pressure.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
                           "question": "Amazon acquired Twitch in August 2014 for $970 million dollars.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean",
                           "difficulty": "easy",
                           "question": "Clefairy was intended to be Ash;s starting Pok&eacute;mon in the pilot episode of the cartoon.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Geography", "type": "boolean", "difficulty": "easy",
                           "question": "A group of islands is called an ;archipelago;.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
                           "question": "Rapper Snoop Dogg;s real name is ;Cordozar Calvin Broadus, Jr.;.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "History", "type": "boolean", "difficulty": "medium",
                           "question": "The first televised presidential debate was between Jimmy Carter and Gerald Ford.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                           "question": "The US emergency hotline is 911 because of the September 11th terrorist attacks.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                           "question": "Steel is an alloy of Iron and Carbon.", "correct_answer": "True",
                           "incorrect_answers": ["False"]},
                          {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                           "question": "Shrimp can swim backwards.", "correct_answer": "True",
                           "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
                           "question": "In the game ;Melty Blood Actress Again Current Code;, you can enter Blood Heat mode in Half Moon style.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
                           "question": "Tony Hawk;s Pro Skater was released in 1999.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Sports", "type": "boolean", "difficulty": "medium",
                           "question": "Tennis was once known as Racquetball.", "correct_answer": "False",
                           "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                           "question": "The Xenomorph from the science fiction film ;Alien; has acidic blood.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                           "question": "Shaquille O;Neal appeared in the 1997 film ;Space Jam;.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "History", "type": "boolean", "difficulty": "medium",
                           "question": "Theodore Roosevelt Jr. was the only General involved in the initial assault on D-Day.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
                           "question": "In Undertale, having a Fun Value set to 56-57 will play the Wrong Number Song Call.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Geography", "type": "boolean", "difficulty": "easy",
                           "question": "There are no deserts in Europe.", "correct_answer": "True",
                           "incorrect_answers": ["False"]},
                          {"category": "History", "type": "boolean", "difficulty": "medium",
                           "question": "In 1967, a magazine published a story about extracting hallucinogenic chemicals from bananas to raise moral questions about banning drugs.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
                           "question": "TF2: The Heavy;s voice actor, Gary Schwartz, voices the Demoman as well ",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean",
                           "difficulty": "easy",
                           "question": "Gosho Aoyama Made This Series: (Detective Conan \/ Case Closed!)",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Science: Gadgets", "type": "boolean", "difficulty": "medium",
                           "question": "The Western Electric Model 500 telephone uses tone dialing to dial phone numbers.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
                           "question": "The Lego Group was founded in 1932.", "correct_answer": "True",
                           "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
                           "question": "In Sonic the Hedgehog universe, Tails; real name is Miles Prower.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
                           "question": "In the original Star Wars trilogy, Alec Guinness provided the voice for Darth Vader.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
                           "question": "Sean Connery wasn;t in Indiana Jones and the Kingdom of the Crystal Skull because he found retirement too enjoyable.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                           "question": "Time on Computers is measured via the EPOX System.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
                           "question": "The names of Roxas;s Keyblades in Kingdom Hearts are Oathkeeper and Oblivion.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
                           "question": "It;s not possible to format a write-protected DVD-R Hard Disk.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Board Games", "type": "boolean", "difficulty": "easy",
                           "question": "PAYDAY: The Heist is a sequel to the board game Payday.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
                           "question": "In Monster Hunter Generations, guild style is a type of hunting style.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Cartoon & Animations", "type": "boolean",
                           "difficulty": "medium",
                           "question": "Nickelodeon rejected the pilot to Adventure Time.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                           "question": "Linux was first created as an alternative to Windows XP.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
                           "question": "In the video game Transistor, Red is the name of the main character.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "History", "type": "boolean", "difficulty": "hard",
                           "question": "The USS Missouri (BB-63) last served in the Korean War.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
                           "question": "The set of all algebraic numbers is countable.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
                           "question": "In Call Of Duty: World At War, the first appearance of the PPSH-41 in Zombies was in the map Der Riese.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
                           "question": "Nick Mason is the only member to appear on every Pink Floyd album.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
                           "question": "The game Pocket Morty has a Morty called Pocket Mortys Morty?",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
                           "question": "Several characters in Super Mario 64 blink their eyes, including Mario himself.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
                           "question": "Hidden in the files for Mario Kart Arcade GP is a picture of the Beslan school hostage crisis.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
                           "question": "Michael Jackson wrote The Simpsons song Do the Bartman.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
                           "question": "The National Animal of Scotland is the Unicorn.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Geography", "type": "boolean", "difficulty": "hard",
                           "question": "The two largest ethnic groups of Belgium are Flemish and Walloon. ",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "History", "type": "boolean", "difficulty": "easy",
                           "question": "The United States of America was the first country to launch a man into space.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "Mythology", "type": "boolean", "difficulty": "hard",
                           "question": "Janus was the Roman god of doorways and passageways.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Music", "type": "boolean", "difficulty": "hard",
                           "question": "The singer Billie Holiday was also known as Lady Day.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Cartoon & Animations", "type": "boolean",
                           "difficulty": "medium",
                           "question": "Donald Duck played the role of Bob Cratchit in Disney;s 1983 adaptation of A Christmas Carol.",
                           "correct_answer": "False", "incorrect_answers": ["True"]},
                          {"category": "History", "type": "boolean", "difficulty": "medium",
                           "question": "Sir Issac Newton served as a Member of Parliament, but the only recorded time he spoke was to complain about a draft in the chambers.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Animals", "type": "boolean", "difficulty": "easy",
                           "question": "The internet browser Firefox is named after the Red Panda.",
                           "correct_answer": "True", "incorrect_answers": ["False"]},
                          {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean",
                           "difficulty": "medium",
                           "question": "In Full Metal Panic!, Whispered are those who are capable of creating Black Technology.",
                           "correct_answer": "True", "incorrect_answers": ["False"]}]
