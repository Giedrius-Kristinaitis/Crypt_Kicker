from input import Input
from output import Output
from typing import Optional

"""
    This whole thing could and, arguably, should be split into smaller services, but I'm lazy right now
"""

class Cypher:

    def decypher(self, data: Input, phrase: str) -> Output:
        result = Output()

        letter_map = self.get_phrase_letter_map(phrase)

        for case in data.cases:
            letters = self.find_letters(case, phrase, letter_map)

            if letters:
                result.add_plaintext(self.decypher_case(letters, case))
            else:
                result.add_plaintext(["No solution"])

        return result

    def get_phrase_letter_map(self, phrase: str) -> dict:
        map = dict()

        for index, letter in enumerate(phrase):
            if letter == ' ' or letter == '\n':
                continue

            if letter not in map.keys():
                map[letter] = []

            map[letter].append(index)

        return map

    def decypher_case(self, letters: dict, case: [str]) -> [str]:
        case_result = []

        for line in case:
            plaintext_line = ""

            for char in line:
                if char == ' ':
                    plaintext_line += ' '
                    continue

                plaintext_line += letters[char]

            case_result.append(plaintext_line + '\n')

        return case_result

    def find_letters(self, case: [str], phrase: str, letter_map: dict) -> Optional[dict]:
        phrase_parts = phrase.split()

        for line in case:
            line_parts = line.split()

            letters = self.extract_letters_from_line(line, phrase_parts, line_parts, letter_map)

            if letters:
                return letters

        return None

    def extract_letters_from_line(self, line: str, phrase_parts: [str], line_parts: [str], letter_map: dict) -> Optional[dict]:
        extracted_letters = dict()

        if len(phrase_parts) != len(line_parts):
            return None

        for i in range(len(phrase_parts)):
            if len(phrase_parts[i]) != len(line_parts[i]) or not self.string_chars_unique(line_parts[i]):
                return None

            for j in range(len(line_parts[i])):
                if line_parts[i][j] in extracted_letters.keys() and phrase_parts[i][j] != extracted_letters[line_parts[i][j]]:
                    return None

                if not self.verify_letter_positions(line, line_parts[i][j], letter_map[phrase_parts[i][j]]):
                    return None

                extracted_letters[line_parts[i][j]] = phrase_parts[i][j]

        return extracted_letters

    def verify_letter_positions(self, line: str, letter: str, positions: [int]) -> bool:
        correct_position_count = 0

        for position, char in enumerate(line):
            if char == letter and position not in positions:
                return False

            if char == letter:
                correct_position_count += 1

        return correct_position_count == len(positions)

    def string_chars_unique(self, string: str) -> bool:
        for i in range(len(string)):
            for j in range(len(string)):
                if i == j:
                    continue

                if string[i] == string[j]:
                    return False

        return True
