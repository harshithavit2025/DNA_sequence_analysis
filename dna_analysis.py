import mysql.connector

# Setting up
def database_setup():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='h2007',
        database='dna_analysis'
    )
    cur = conn.cursor()

    # Create tables if they don't already exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS dna_sequences (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            sequence VARCHAR(255),
            is_valid BOOLEAN
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS dna_analysis_results (
            seq_ID INT,
            match_status VARCHAR(20),
            base_a_count VARCHAR(10),
            replaced_seq VARCHAR(255),
            FOREIGN KEY (seq_ID) REFERENCES dna_sequences(ID)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS rna_seq (
            seq_ID INT,
            rna_sequence VARCHAR(255),
            pattern VARCHAR(50),
            pattern_position VARCHAR(50),
            FOREIGN KEY (seq_ID) REFERENCES dna_sequences(ID)
        )
    """)

    conn.commit()
    return conn, cur


# Defining required functions
def is_valid_dna(seq):
    valid_bases = {'A', 'T', 'G', 'C'}  # set of valid bases
    for base in seq:
        if base not in valid_bases:
            return False
    return True


def complement(seq):
    mapping = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp = ''
    for base in seq:
        comp += mapping.get(base, base)
    return comp


def base_frequency(valid_sequences):
    base_freq = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for seq in valid_sequences:
        for b in seq:
            if b in base_freq:
                base_freq[b] += 1
    return base_freq


# Main logic
def main():
    conn, cur = database_setup()

    n = int(input("Enter number of DNA sequences: "))
    sequences = []
    for i in range(n):
        seq = input(f"Enter DNA sequence {i + 1}: ").upper()
        valid = is_valid_dna(seq)
        cur.execute("INSERT INTO dna_sequences(sequence, is_valid) VALUES (%s, %s)", (seq, valid))
        sequences.append((seq, valid))
    conn.commit()

    search_seq = input("Enter specific sequence to search: ").upper()
    base = input("Enter base to count (A/T/G/C): ").upper()

    valid_sequences = [seq for seq, valid in sequences if valid]
    base_freq = base_frequency(valid_sequences)

    validation_results = []
    match_results = []
    count_results = []
    replace_results = []
    rna_results = []
    pattern_results = []
    complement_results = []

    for seq_id, (seq, valid) in enumerate(sequences, start=1):
        if not valid:
            validation_results.append(f"DNA sequence {seq_id}: Invalid")
            match_results.append(f"DNA sequence {seq_id}: No Match")
            count_results.append(f"DNA sequence {seq_id}: -")
            continue

        validation_results.append(f"DNA sequence {seq_id}: Valid")

        match_status = "Match" if search_seq in seq else "No Match"
        match_results.append(f"DNA sequence {seq_id}: {match_status}")

        base_count = seq.count(base)
        count_results.append(f"DNA sequence {seq_id}: {base_count}")


    conn.commit()
    conn.close()

    # Printing the outputs
    print()
    print("Validation Results:")
    for line in validation_results:
        print(line)
    print()
    print("Match Results")
    for line in match_results:
        print(line)
    print()
    print("Specific Base Count Results:")
    for line in count_results:
        print(line)
    print()
    print(f"Frequency of Unique Bases: {base_freq}")

# Execute
if __name__ == "__main__":
    main()

