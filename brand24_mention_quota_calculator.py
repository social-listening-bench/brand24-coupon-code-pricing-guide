#!/usr/bin/env python3
"""
Brand24 Subscription Quota & Annual Savings Calculator 2026.
"""
import argparse

PLANS = {
    "individual": {"monthly": 99.0, "annual": 79.0, "mentions": 2000, "keywords": 3},
    "team": {"monthly": 179.0, "annual": 149.0, "mentions": 5000, "keywords": 7},
    "pro": {"monthly": 249.0, "annual": 199.0, "mentions": 25000, "keywords": 12},
    "enterprise": {"monthly": 499.0, "annual": 399.0, "mentions": 100000, "keywords": 25}
}

def calculate(plan, annual):
    p = PLANS.get(plan.lower(), PLANS["team"])
    monthly_rate = p["annual"] if annual else p["monthly"]
    annual_spend = monthly_rate * 12.0
    savings = (p["monthly"] - p["annual"]) * 12.0 if annual else 0.0

    print("=" * 60)
    print(f"Brand24 Social Listening Calculator - Plan: {plan.upper()}")
    print("=" * 60)
    print(f"Keyword Triggers:        {p['keywords']} tracked keywords")
    print(f"Monthly Mention Quota:   {p['mentions']:,} mentions/mo")
    print(f"Monthly Plan Rate:       ${monthly_rate:.2f}/mo ({'Annual 20% Off' if annual else 'Monthly'})")
    print(f"Annual Total Spend:      ${annual_spend:,.2f}/year")
    if annual:
        print(f"Annual Discount Savings: ${savings:,.2f}/year")
    print("=" * 60)
    return monthly_rate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brand24 Pricing Calculator")
    parser.add_argument("--plan", default="team", choices=["individual", "team", "pro", "enterprise"])
    parser.add_argument("--annual", action="store_true", default=True)
    args = parser.parse_args()
    calculate(args.plan, args.annual)
