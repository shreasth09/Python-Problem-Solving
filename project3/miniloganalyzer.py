# 📊 Mini Log Analyzer (CLI Based)

from collections import Counter


# Analyze logs
def analyze_logs(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        error = 0
        warning = 0
        info = 0
        messages = []

        for line in lines:
            if "ERROR" in line:
                error += 1
                messages.append(line.strip())
            elif "WARNING" in line:
                warning += 1
            elif "INFO" in line:
                info += 1

        print("\n📊 LOG SUMMARY")
        print("ERROR:", error)
        print("WARNING:", warning)
        print("INFO:", info)

        # Most frequent error messages
        freq = Counter(messages)
        print("\n🔝 Frequent Errors:")
        for msg, count in freq.most_common(5):
            print(msg, ":", count)

    except FileNotFoundError:
        print("❌ File not found")


# Search logs
def search_logs(filename, keyword):
    with open(filename, "r") as f:
        found = False
        for i, line in enumerate(f, 1):
            if keyword in line:
                print(f"Line {i}: {line.strip()}")
                found = True

        if not found:
            print("No matching logs found")


# Filter by date
def filter_by_date(filename, date):
    with open(filename, "r") as f:
        for line in f:
            if date in line:
                print(line.strip())


# Export report
def export_report(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    error = sum(1 for line in lines if "ERROR" in line)
    warning = sum(1 for line in lines if "WARNING" in line)
    info = sum(1 for line in lines if "INFO" in line)

    with open("log_report.txt", "w") as f:
        f.write("LOG ANALYSIS REPORT\n")
        f.write(f"ERROR: {error}\n")
        f.write(f"WARNING: {warning}\n")
        f.write(f"INFO: {info}\n")

    print("✅ Report saved as log_report.txt")


# Main menu
def main():
    filename = input("Enter log file name: ")

    while True:
        print("\n==== LOG ANALYZER ====")
        print("1. Analyze Logs")
        print("2. Search Logs")
        print("3. Filter by Date")
        print("4. Export Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            analyze_logs(filename)

        elif choice == "2":
            keyword = input("Enter keyword: ")
            search_logs(filename, keyword)

        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            filter_by_date(filename, date)

        elif choice == "4":
            export_report(filename)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()