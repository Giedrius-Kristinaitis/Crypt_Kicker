class Input:

    cases = []

    def process(self, lines: [str]) -> None:
        current_case = []

        for line in lines:
            line = line.rstrip()

            if line.isnumeric():
                continue

            if not line and current_case:
                self.cases.append(current_case)
                current_case = []
            elif line:
                current_case.append(line)

        if current_case:
            self.cases.append(current_case)

    def populate_from_file(self, file_name: str) -> None:
        file = open(file_name, 'r')

        lines = file.readlines()

        file.close()

        self.process(lines)
