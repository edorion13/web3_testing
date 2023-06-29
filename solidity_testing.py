from web3 import Web3
import json


ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# setting the defualt account as the company account (deployed account)
web3.eth.default_account = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"loanId","type":"uint256"},{"indexed":false,"internalType":"address","name":"borrower","type":"address"},{"indexed":false,"internalType":"uint256","name":"loanAmount","type":"uint256"}],"name":"LoanCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"loanId","type":"uint256"}],"name":"LoanFullyRepaid","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"loanId","type":"uint256"},{"indexed":false,"internalType":"address","name":"lender","type":"address"},{"indexed":false,"internalType":"uint256","name":"fundAmount","type":"uint256"}],"name":"LoanFunded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"loanId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"repaymentAmount","type":"uint256"}],"name":"LoanPayment","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_loanAmount","type":"uint256"},{"internalType":"uint256","name":"_interestRate","type":"uint256"},{"internalType":"uint256","name":"_repaymentTerm","type":"uint256"}],"name":"createLoan","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_loanId","type":"uint256"}],"name":"fundLoan","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_loanId","type":"uint256"}],"name":"getLoanDetails","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bool","name":"","type":"bool"},{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"loanIdCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"loans","outputs":[{"internalType":"uint256","name":"loanId","type":"uint256"},{"internalType":"address payable","name":"borrower","type":"address"},{"internalType":"address payable","name":"lender","type":"address"},{"internalType":"uint256","name":"loanAmount","type":"uint256"},{"internalType":"uint256","name":"interestRate","type":"uint256"},{"internalType":"uint256","name":"repaymentTerm","type":"uint256"},{"internalType":"uint256","name":"fundAmount","type":"uint256"},{"internalType":"uint256","name":"amountPayed","type":"uint256"},{"internalType":"bool","name":"funded","type":"bool"},{"internalType":"bool","name":"repaid","type":"bool"},{"internalType":"uint256","name":"balanceRemaning","type":"uint256"},{"internalType":"uint256","name":"amountOwed","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_loanId","type":"uint256"}],"name":"repayLoan","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
bytecode =  "6080604052600160035534801561001557600080fd5b5033600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790556000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550611142806100a46000396000f3fe6080604052600436106100705760003560e01c80639d939d161161004e5780639d939d16146101dd578063ab7b1c8914610208578063d0e30db014610236578063e1ec3c681461024057610070565b806366877b8d14610072578063846b909a14610160578063904b513b1461018e575b005b34801561007e57600080fd5b506100ab6004803603602081101561009557600080fd5b810190808035906020019092919050505061033c565b604051808b81526020018a73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200188815260200187815260200186815260200185815260200184815260200183151515158152602001821515151581526020019a505050505050505050505060405180910390f35b61018c6004803603602081101561017657600080fd5b8101908080359060200190929190505050610584565b005b34801561019a57600080fd5b506101db600480360360608110156101b157600080fd5b8101908080359060200190929190803590602001909291908035906020019092919050505061085d565b005b3480156101e957600080fd5b506101f2610bdd565b6040518082815260200191505060405180910390f35b6102346004803603602081101561021e57600080fd5b8101908080359060200190929190505050610be3565b005b61023e610f21565b005b34801561024c57600080fd5b506102796004803603602081101561026357600080fd5b8101908080359060200190929190505050610f23565b604051808d81526020018c73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018b73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018a815260200189815260200188815260200187815260200186815260200185151515158152602001841515151581526020018381526020018281526020019c5050505050505050505050505060405180910390f35b6000806000806000806000806000806004805490508b106103c5576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f496e76616c6964206c6f616e204944000000000000000000000000000000000081525060200191505060405180910390fd5b6103cd610fea565b60048c815481106103da57fe5b90600052602060002090600b020160405180610180016040529081600082015481526020016001820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020016002820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200160038201548152602001600482015481526020016005820154815260200160068201548152602001600782015481526020016008820160009054906101000a900460ff161515151581526020016008820160019054906101000a900460ff1615151515815260200160098201548152602001600a820154815250509050806000015181602001518260400151836060015184608001518560a001518660c001518760e001518861010001518961012001518898508797509a509a509a509a509a509a509a509a509a509a50509193959799509193959799565b60006004828154811061059357fe5b90600052602060002090600b020190508060080160009054906101000a900460ff1615610628576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f4c6f616e2068617320616c7265616479206265656e2066756e6465640000000081525060200191505060405180910390fd5b80600301543410156106a2576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260208152602001807f496e73756666696369656e742066756e647320746f20636f766572206c6f616e81525060200191505060405180910390fd5b8060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc82600301549081150290604051600060405180830381858888f19350505050158015610710573d6000803e3d6000fd5b50338160020160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060018160080160006101000a81548160ff0219169083151502179055508060030154816006018190555080600301548160090181905550806003015481600a01819055506000349050606460018202816107aa57fe5b04600381905550606460018360040154023402816107c457fe5b0482600a018190555060035482600a01600082825401925050819055507fbd7ef6c6281278f6c8ac4ae9ef2f205b52425813c288dd47c377cb6b59c5076e83338460030154604051808481526020018373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001828152602001935050505060405180910390a1505050565b600083116108b6576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260228152602001806110c86022913960400191505060405180910390fd5b6000821161090f576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260248152602001806110ea6024913960400191505060405180910390fd5b60008111610968576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602581526020018061107c6025913960400191505060405180910390fd5b600060056000815480929190600101919050559050610985610fea565b6040518061018001604052808381526020013373ffffffffffffffffffffffffffffffffffffffff168152602001600073ffffffffffffffffffffffffffffffffffffffff168152602001868152602001858152602001848152602001600081526020016000815260200160001515815260200160001515815260200160008152602001600081525090506004819080600181540180825580915050906001820390600052602060002090600b0201600090919290919091506000820151816000015560208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060408201518160020160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550606082015181600301556080820151816004015560a0820151816005015560c0820151816006015560e082015181600701556101008201518160080160006101000a81548160ff0219169083151502179055506101208201518160080160016101000a81548160ff021916908315150217905550610140820151816009015561016082015181600a01555050507f8910ba13a55695f056e224bbbc6b65d866b12a8c2fbdf387fb853a1cca298cd7823387604051808481526020018373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001828152602001935050505060405180910390a15050505050565b60055481565b600060048281548110610bf257fe5b90600052602060002090600b020190508060080160009054906101000a900460ff16610c86576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260188152602001807f4c6f616e20686173206e6f74206265656e2066756e646564000000000000000081525060200191505060405180910390fd5b8060080160019054906101000a900460ff1615610d0b576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f4c6f616e2068617320616c7265616479206265656e207265706169640000000081525060200191505060405180910390fd5b60003411610d64576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260278152602001806110a16027913960400191505060405180910390fd5b6000349050600060646001830281610d7857fe5b049050600081830390506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc839081150290604051600060405180830381858888f19350505050158015610de9573d6000803e3d6000fd5b508360020160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc829081150290604051600060405180830381858888f19350505050158015610e54573d6000803e3d6000fd5b50828460090160008282540392505081905550828460070160008282540192505081905550600084600901541415610edb5760018460080160016101000a81548160ff0219169083151502179055507f6a65a58027e68282a85ac65a7afc6580ef3d139c6e6ec12ae8d82de13566e8cc856040518082815260200191505060405180910390a15b7fc10d13ca243ce0fb173fd7989f1717563a49330d773e2907705ff93ceb7276a08534604051808381526020018281526020019250505060405180910390a15050505050565b565b60048181548110610f3057fe5b90600052602060002090600b02016000915090508060000154908060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060020160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060030154908060040154908060050154908060060154908060070154908060080160009054906101000a900460ff16908060080160019054906101000a900460ff169080600901549080600a015490508c565b60405180610180016040528060008152602001600073ffffffffffffffffffffffffffffffffffffffff168152602001600073ffffffffffffffffffffffffffffffffffffffff16815260200160008152602001600081526020016000815260200160008152602001600081526020016000151581526020016000151581526020016000815260200160008152509056fe52657061796d656e74207465726d206d7573742062652067726561746572207468616e203052657061796d656e7420616d6f756e74206d7573742062652067726561746572207468616e20304c6f616e20616d6f756e74206d7573742062652067726561746572207468616e2030496e7465726573742072617465206d7573742062652067726561746572207468616e2030a265627a7a7231582068e001504801d4c479d9e1e0a181dd29520d14e424844177862663de7be606b964736f6c63430005110032",

Greeter = web3.eth.contract(abi=abi, bytecode = bytecode)

tx_hash = Greeter.constructor().transact()

print(tx_hash)