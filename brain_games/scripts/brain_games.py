#!/usr/bin/env python3
import sys
sys.path.append("../../brain_games")
from brain_games import cli

def main():
	print("Welcome to the Brain Games!")
	cli.welcome_user()
	name = cli.name

if __name__=="__main__":
	main()
