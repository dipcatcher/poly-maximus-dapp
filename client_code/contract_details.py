import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

def get_contract_details(ticker):
  tokens = {
    "POLY": {
      'address' :"0xFd9cf3a413cED20C68028116EEB1EdcA434B7998",
      'abi' : [
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "mint_duration",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "nonpayable",
  		"type": "constructor"
  	},
  	{
  		"anonymous": False,
  		"inputs": [
  			{
  				"indexed": True,
  				"internalType": "address",
  				"name": "owner",
  				"type": "address"
  			},
  			{
  				"indexed": True,
  				"internalType": "address",
  				"name": "spender",
  				"type": "address"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "value",
  				"type": "uint256"
  			}
  		],
  		"name": "Approval",
  		"type": "event"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "spender",
  				"type": "address"
  			},
  			{
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			}
  		],
  		"name": "approve",
  		"outputs": [
  			{
  				"internalType": "bool",
  				"name": "",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "liquidationId",
  				"type": "uint256"
  			},
  			{
  				"internalType": "uint256",
  				"name": "liquidationBid",
  				"type": "uint256"
  			}
  		],
  		"name": "bid",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"anonymous": False,
  		"inputs": [
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "liquidationId",
  				"type": "uint256"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "liquidationBid",
  				"type": "uint256"
  			}
  		],
  		"name": "Bid",
  		"type": "event"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			}
  		],
  		"name": "burn",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "account",
  				"type": "address"
  			},
  			{
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			}
  		],
  		"name": "burnFrom",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "spender",
  				"type": "address"
  			},
  			{
  				"internalType": "uint256",
  				"name": "subtractedValue",
  				"type": "uint256"
  			}
  		],
  		"name": "decreaseAllowance",
  		"outputs": [
  			{
  				"internalType": "bool",
  				"name": "",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "hsiIndex",
  				"type": "uint256"
  			},
  			{
  				"internalType": "address",
  				"name": "hsiAddress",
  				"type": "address"
  			}
  		],
  		"name": "endHSIStake",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "stakeIndex",
  				"type": "uint256"
  			},
  			{
  				"internalType": "uint40",
  				"name": "stakeIdParam",
  				"type": "uint40"
  			}
  		],
  		"name": "endNativeStake",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "finalizeMinting",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "spender",
  				"type": "address"
  			},
  			{
  				"internalType": "uint256",
  				"name": "addedValue",
  				"type": "uint256"
  			}
  		],
  		"name": "increaseAllowance",
  		"outputs": [
  			{
  				"internalType": "bool",
  				"name": "",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"anonymous": False,
  		"inputs": [
  			{
  				"indexed": True,
  				"internalType": "address",
  				"name": "user",
  				"type": "address"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			}
  		],
  		"name": "Mint",
  		"type": "event"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			},
  			{
  				"internalType": "uint256",
  				"name": "bid_budget_percent",
  				"type": "uint256"
  			}
  		],
  		"name": "mintPoly",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "hsi_id",
  				"type": "uint256"
  			}
  		],
  		"name": "processHSI",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"anonymous": False,
  		"inputs": [
  			{
  				"indexed": True,
  				"internalType": "address",
  				"name": "hsi_address",
  				"type": "address"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "hsi_id",
  				"type": "uint256"
  			}
  		],
  		"name": "ProcessHSI",
  		"type": "event"
  	},
  	{
  		"anonymous": False,
  		"inputs": [
  			{
  				"indexed": True,
  				"internalType": "address",
  				"name": "user",
  				"type": "address"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "hex_redeemed",
  				"type": "uint256"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "hedron_redeemed",
  				"type": "uint256"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "icosa_redeemed",
  				"type": "uint256"
  			}
  		],
  		"name": "Redeem",
  		"type": "event"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			}
  		],
  		"name": "redeemPoly",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "restake_leftover",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "stake_leftover_hdrn",
  		"outputs": [],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "to",
  				"type": "address"
  			},
  			{
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			}
  		],
  		"name": "transfer",
  		"outputs": [
  			{
  				"internalType": "bool",
  				"name": "",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"anonymous": False,
  		"inputs": [
  			{
  				"indexed": True,
  				"internalType": "address",
  				"name": "from",
  				"type": "address"
  			},
  			{
  				"indexed": True,
  				"internalType": "address",
  				"name": "to",
  				"type": "address"
  			},
  			{
  				"indexed": False,
  				"internalType": "uint256",
  				"name": "value",
  				"type": "uint256"
  			}
  		],
  		"name": "Transfer",
  		"type": "event"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "from",
  				"type": "address"
  			},
  			{
  				"internalType": "address",
  				"name": "to",
  				"type": "address"
  			},
  			{
  				"internalType": "uint256",
  				"name": "amount",
  				"type": "uint256"
  			}
  		],
  		"name": "transferFrom",
  		"outputs": [
  			{
  				"internalType": "bool",
  				"name": "",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "owner",
  				"type": "address"
  			},
  			{
  				"internalType": "address",
  				"name": "spender",
  				"type": "address"
  			}
  		],
  		"name": "allowance",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "account",
  				"type": "address"
  			}
  		],
  		"name": "balanceOf",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "bidding_budget_percent",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "BIDDING_BUDGET_TRACKER",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "balance",
  				"type": "uint256"
  			},
  			{
  				"internalType": "uint256",
  				"name": "supply",
  				"type": "uint256"
  			}
  		],
  		"name": "calculate_redemption_rate",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "redemption_rate",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "decimals",
  		"outputs": [
  			{
  				"internalType": "uint8",
  				"name": "",
  				"type": "uint8"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "DID_STAKE_LEFTOVER",
  		"outputs": [
  			{
  				"internalType": "bool",
  				"name": "",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "getCurrentDay",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "hex_day",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "uint256",
  				"name": "liquidation_index",
  				"type": "uint256"
  			}
  		],
  		"name": "getLiquidation",
  		"outputs": [
  			{
  				"components": [
  					{
  						"internalType": "uint16",
  						"name": "mintedDays",
  						"type": "uint16"
  					},
  					{
  						"internalType": "uint8",
  						"name": "launchBonus",
  						"type": "uint8"
  					},
  					{
  						"internalType": "uint16",
  						"name": "loanStart",
  						"type": "uint16"
  					},
  					{
  						"internalType": "uint16",
  						"name": "loanedDays",
  						"type": "uint16"
  					},
  					{
  						"internalType": "uint32",
  						"name": "interestRate",
  						"type": "uint32"
  					},
  					{
  						"internalType": "uint8",
  						"name": "paymentsMade",
  						"type": "uint8"
  					},
  					{
  						"internalType": "bool",
  						"name": "isLoaned",
  						"type": "bool"
  					},
  					{
  						"internalType": "uint256",
  						"name": "liquidationStart",
  						"type": "uint256"
  					},
  					{
  						"internalType": "address",
  						"name": "hsiAddress",
  						"type": "address"
  					},
  					{
  						"internalType": "uint96",
  						"name": "bidAmount",
  						"type": "uint96"
  					},
  					{
  						"internalType": "address",
  						"name": "liquidator",
  						"type": "address"
  					},
  					{
  						"internalType": "uint88",
  						"name": "endOffset",
  						"type": "uint88"
  					},
  					{
  						"internalType": "bool",
  						"name": "isActive",
  						"type": "bool"
  					}
  				],
  				"internalType": "struct PolyMaximus.LiquidationData",
  				"name": "liquidation_data",
  				"type": "tuple"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "HDRN_STAKING_BUDGET",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "HEDRON_REDEMPTION_RATE",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "HEX_REDEMPTION_RATE",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [
  			{
  				"internalType": "address",
  				"name": "",
  				"type": "address"
  			}
  		],
  		"name": "HEXStakes",
  		"outputs": [
  			{
  				"internalType": "uint40",
  				"name": "stakeId",
  				"type": "uint40"
  			},
  			{
  				"internalType": "uint72",
  				"name": "stakedHearts",
  				"type": "uint72"
  			},
  			{
  				"internalType": "uint72",
  				"name": "stakeShares",
  				"type": "uint72"
  			},
  			{
  				"internalType": "uint16",
  				"name": "lockedDay",
  				"type": "uint16"
  			},
  			{
  				"internalType": "uint16",
  				"name": "stakedDays",
  				"type": "uint16"
  			},
  			{
  				"internalType": "uint16",
  				"name": "unlockedDay",
  				"type": "uint16"
  			},
  			{
  				"internalType": "bool",
  				"name": "isAutoStake",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "ICOSA_CONTRACT_ADDRESS",
  		"outputs": [
  			{
  				"internalType": "address",
  				"name": "",
  				"type": "address"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "ICOSA_REDEMPTION_RATE",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "IS_REDEMPTION_ACTIVE",
  		"outputs": [
  			{
  				"internalType": "bool",
  				"name": "",
  				"type": "bool"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "LAST_ACTIVE_HSI",
  		"outputs": [
  			{
  				"internalType": "address",
  				"name": "",
  				"type": "address"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "LAST_STAKE_START_DAY",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "LATEST_STAKE_END_DAY",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "MINTING_PHASE_END",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "MINTING_PHASE_START",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "name",
  		"outputs": [
  			{
  				"internalType": "string",
  				"name": "",
  				"type": "string"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "STAKING_BUDGET_TRACKER",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "symbol",
  		"outputs": [
  			{
  				"internalType": "string",
  				"name": "",
  				"type": "string"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "THANK_YOU_TEAM",
  		"outputs": [
  			{
  				"internalType": "address",
  				"name": "",
  				"type": "address"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "TOTAL_BIDDING_BUDGET",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	},
  	{
  		"inputs": [],
  		"name": "totalSupply",
  		"outputs": [
  			{
  				"internalType": "uint256",
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"stateMutability": "view",
  		"type": "function"
  	}
]
    },
    "WATER": {
      'address' :"0xa5a46f40E5c01E6D6758B4E39714630f2ce2a3d4",
      'abi' : [
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "executor_address",
      				"type": "address"
      			}
      		],
      		"stateMutability": "nonpayable",
      		"type": "constructor"
      	},
      	{
      		"anonymous": False,
      		"inputs": [
      			{
      				"indexed": True,
      				"internalType": "address",
      				"name": "owner",
      				"type": "address"
      			},
      			{
      				"indexed": True,
      				"internalType": "address",
      				"name": "spender",
      				"type": "address"
      			},
      			{
      				"indexed": False,
      				"internalType": "uint256",
      				"name": "value",
      				"type": "uint256"
      			}
      		],
      		"name": "Approval",
      		"type": "event"
      	},
      	{
      		"anonymous": False,
      		"inputs": [
      			{
      				"indexed": True,
      				"internalType": "address",
      				"name": "flusher",
      				"type": "address"
      			},
      			{
      				"indexed": False,
      				"internalType": "uint256",
      				"name": "amount",
      				"type": "uint256"
      			}
      		],
      		"name": "Flush",
      		"type": "event"
      	},
      	{
      		"anonymous": False,
      		"inputs": [
      			{
      				"indexed": True,
      				"internalType": "address",
      				"name": "minter",
      				"type": "address"
      			},
      			{
      				"indexed": False,
      				"internalType": "uint256",
      				"name": "mint_rate",
      				"type": "uint256"
      			},
      			{
      				"indexed": False,
      				"internalType": "uint256",
      				"name": "amount",
      				"type": "uint256"
      			}
      		],
      		"name": "Mint",
      		"type": "event"
      	},
      	{
      		"anonymous": False,
      		"inputs": [
      			{
      				"indexed": True,
      				"internalType": "address",
      				"name": "from",
      				"type": "address"
      			},
      			{
      				"indexed": True,
      				"internalType": "address",
      				"name": "to",
      				"type": "address"
      			},
      			{
      				"indexed": False,
      				"internalType": "uint256",
      				"name": "value",
      				"type": "uint256"
      			}
      		],
      		"name": "Transfer",
      		"type": "event"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "owner",
      				"type": "address"
      			},
      			{
      				"internalType": "address",
      				"name": "spender",
      				"type": "address"
      			}
      		],
      		"name": "allowance",
      		"outputs": [
      			{
      				"internalType": "uint256",
      				"name": "",
      				"type": "uint256"
      			}
      		],
      		"stateMutability": "view",
      		"type": "function"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "spender",
      				"type": "address"
      			},
      			{
      				"internalType": "uint256",
      				"name": "amount",
      				"type": "uint256"
      			}
      		],
      		"name": "approve",
      		"outputs": [
      			{
      				"internalType": "bool",
      				"name": "",
      				"type": "bool"
      			}
      		],
      		"stateMutability": "nonpayable",
      		"type": "function"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "account",
      				"type": "address"
      			}
      		],
      		"name": "balanceOf",
      		"outputs": [
      			{
      				"internalType": "uint256",
      				"name": "",
      				"type": "uint256"
      			}
      		],
      		"stateMutability": "view",
      		"type": "function"
      	},
      	{
      		"inputs": [],
      		"name": "current_mint_rate",
      		"outputs": [
      			{
      				"internalType": "uint256",
      				"name": "",
      				"type": "uint256"
      			}
      		],
      		"stateMutability": "view",
      		"type": "function"
      	},
      	{
      		"inputs": [],
      		"name": "decimals",
      		"outputs": [
      			{
      				"internalType": "uint8",
      				"name": "",
      				"type": "uint8"
      			}
      		],
      		"stateMutability": "view",
      		"type": "function"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "spender",
      				"type": "address"
      			},
      			{
      				"internalType": "uint256",
      				"name": "subtractedValue",
      				"type": "uint256"
      			}
      		],
      		"name": "decreaseAllowance",
      		"outputs": [
      			{
      				"internalType": "bool",
      				"name": "",
      				"type": "bool"
      			}
      		],
      		"stateMutability": "nonpayable",
      		"type": "function"
      	},
      	{
      		"inputs": [],
      		"name": "flush",
      		"outputs": [],
      		"stateMutability": "nonpayable",
      		"type": "function"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "token_contract_address",
      				"type": "address"
      			}
      		],
      		"name": "flush_erc20",
      		"outputs": [],
      		"stateMutability": "nonpayable",
      		"type": "function"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "spender",
      				"type": "address"
      			},
      			{
      				"internalType": "uint256",
      				"name": "addedValue",
      				"type": "uint256"
      			}
      		],
      		"name": "increaseAllowance",
      		"outputs": [
      			{
      				"internalType": "bool",
      				"name": "",
      				"type": "bool"
      			}
      		],
      		"stateMutability": "nonpayable",
      		"type": "function"
      	},
      	{
      		"inputs": [],
      		"name": "name",
      		"outputs": [
      			{
      				"internalType": "string",
      				"name": "",
      				"type": "string"
      			}
      		],
      		"stateMutability": "view",
      		"type": "function"
      	},
      	{
      		"inputs": [],
      		"name": "symbol",
      		"outputs": [
      			{
      				"internalType": "string",
      				"name": "",
      				"type": "string"
      			}
      		],
      		"stateMutability": "view",
      		"type": "function"
      	},
      	{
      		"inputs": [],
      		"name": "totalSupply",
      		"outputs": [
      			{
      				"internalType": "uint256",
      				"name": "",
      				"type": "uint256"
      			}
      		],
      		"stateMutability": "view",
      		"type": "function"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "to",
      				"type": "address"
      			},
      			{
      				"internalType": "uint256",
      				"name": "amount",
      				"type": "uint256"
      			}
      		],
      		"name": "transfer",
      		"outputs": [
      			{
      				"internalType": "bool",
      				"name": "",
      				"type": "bool"
      			}
      		],
      		"stateMutability": "nonpayable",
      		"type": "function"
      	},
      	{
      		"inputs": [
      			{
      				"internalType": "address",
      				"name": "from",
      				"type": "address"
      			},
      			{
      				"internalType": "address",
      				"name": "to",
      				"type": "address"
      			},
      			{
      				"internalType": "uint256",
      				"name": "amount",
      				"type": "uint256"
      			}
      		],
      		"name": "transferFrom",
      		"outputs": [
      			{
      				"internalType": "bool",
      				"name": "",
      				"type": "bool"
      			}
      		],
      		"stateMutability": "nonpayable",
      		"type": "function"
      	},
      	{
      		"stateMutability": "payable",
      		"type": "receive"
      	}
      ]
              
          }
    
  }
  return tokens[ticker]['address'], tokens[ticker]['abi']
