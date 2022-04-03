import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--per-day", type=float, default=0)
parser.add_argument("--per-week", type=float, default=0)
parser.add_argument("--per-month", type=float, default=0)
parser.add_argument("--per-year", type=float, default=0)
parser.add_argument("--get-by", type=str, default="day", choices=["day", "month", "year"])
args = parser.parse_args()
profit = args.per_day + args.per_week / 7 + args.per_month / 30 + args.per_year / 360
if args.get_by == "day":
    pass
elif args.get_by == "month":
    profit = int(profit * 7)
elif args.get_by == "year":
    profit = int(profit * 360)
print(int(profit))
