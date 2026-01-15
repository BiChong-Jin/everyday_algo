import sys


def parse_time(ts: str):
    # "YYYY/MM/DD-hh:mm:ss"
    y = int(ts[0:4])
    m = int(ts[5:7])
    d = int(ts[8:10])
    hh = int(ts[11:13])
    mm = int(ts[14:16])
    ss = int(ts[17:19])
    return (y, m, d, hh, mm, ss)


class User:
    pass


class Plan:
    def __init__(self, plan_id, name, monthly_cost, monthly_price) -> None:
        self.plan_id = plan_id
        self.name = name
        self.monthly_cost = monthly_cost
        self.monthly_price = monthly_price
        self.deleted_flag = False


class Subsctiption:
    def __init__(self, subscription_id, user_id, plan_id, start_time, end_time) -> None:
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.plan_id = plan_id
        self.start_time = start_time
        self.end_time = end_time
        # 0: active, 1: canceld, 2: expied
        self.status = 0


class Transaction:
    def __init__(self, user_id, plan_id, amount, cost, time) -> None:
        self.user_id = user_id
        self.plan_id = plan_id
        self.amount = amount
        self.cost = cost
        self.time = time
        # 0:charge, 1: refund
        self.types = 0


if __name__ == "__main__":
    input = sys.stdin.readline

    rate_str = input()
    if "." in rate_str:
        a, b = rate_str.split(".")
        b = (b + "00")[:2]
        rate_int = int(a) * 100 + int(b)
    else:
        rate_int = int(rate_str) * 100

    created_plan = set()

    user_cnt = int(input())
    user_name = []

    for i in range(user_cnt):
        curr_user_name = input()
        user_name.append(curr_user_name)

    def cond_margin_ok(S, C):
        # (S-C)/S >= rate  <=>  100*(S-C) >= rate_int * S
        return 100 * (S - C) >= rate_int * S

    query_cnt = int(input())
    queries = []

    for i in range(query_cnt):
        line = input().strip()
        if line.startswith("create-plan: "):
            _, rest = line.split(": ")
            t_str, plan_name, monthly_cost_str, monthly_price_str = rest.split()
            t = parse_time(t_str)
            monthly_cost = int(monthly_cost_str)
            monthly_price = int(monthly_price_str)

            if plan_name in created_plan:
                print("Plan already exsits.")

            elif cond_margin_ok(monthly_price, monthly_cost):
                print("create-plan: ")
