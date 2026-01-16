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
    def __init__(self, user_id, name) -> None:
        self.user_id = user_id
        self.name = name
        self.active_sub = None


class Plan:
    def __init__(self, name, monthly_cost, monthly_price) -> None:
        self.name = name
        self.monthly_cost = monthly_cost
        self.monthly_price = monthly_price
        self.deleted = False


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

    plans = {}  # user_id -> Plan()
    plan_name_to_id = {}  # plan_name -> plan_id

    user_cnt = int(input())
    user_name = []
    users = [0] * (user_cnt + 1)

    for i in range(user_cnt):
        curr_user_name = input()
        user_name.append(curr_user_name)

    def cond_margin_ok(S, C):
        # (S-C)/S >= rate  <=>  100*(S-C) >= rate_int * S
        return 100 * (S - C) >= rate_int * S

    query_cnt = int(input())
    queries = []

    next_plan_id = 1
    next_subscribe_id = 1
    subcribes = [None] * query_cnt

    for i in range(query_cnt):
        line = input().strip()
        if line.startswith("create-plan: "):
            _, rest = line.split(": ")
            t_str, plan_name, monthly_cost_str, monthly_price_str = rest.split()
            t = parse_time(t_str)
            monthly_cost = int(monthly_cost_str)
            monthly_price = int(monthly_price_str)

            if plan_name in plan_name_to_id:
                print("Plan already exsits.")
                continue

            elif cond_margin_ok(monthly_price, monthly_cost):
                print("create-plan: f{next_plan_id}")
                plan_name_to_id[plan_name] = next_plan_id
                plans[next_plan_id] = Plan(plan_name, monthly_cost, monthly_price)

                next_plan_id += 1

        elif line.startswith("subscribe"):
            _, rest = line.split(": ")
            t_str, user_id, plan_id = rest.split()
            t = parse_time(t_str)

            if plan_id not in plans:
                print("Plan does not exsits.")
                continue
            if plans[plan_id].deleted:
                print("Plan has been deleted.")
                continue
            if users[user_id].active_sub != None:
                print(
                    "f{user_id} already has subscription f{user_sub_status[user_id].active_sub}."
                )
                continue

            users[user_id].active_sub = next_subscribe_id
            subcribes[next_subscribe_id] = Subsctiption(
                next_subscribe_id, user_id, plan_id, t, None
            )
            next_subscribe_id += 1
