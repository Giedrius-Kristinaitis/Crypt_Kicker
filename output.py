class Output:

    plaintext = []

    def add_plaintext(self, text: [str]) -> None:
        self.plaintext.append(text)

    def print_to_file(self, file_name: str) -> None:
        file = open(file_name, 'w')

        for output_case in self.plaintext:
            file.writelines(output_case)
            file.write('\n')

        file.close()
