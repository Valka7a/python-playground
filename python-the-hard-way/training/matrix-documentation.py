"""
var _printMatrix = function (name, matrix) {
    console.log(name);

    for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < matrix[i].length; j++) {
            process.stdout.write(('000' + matrix[i][j]).slice(-2).toString() + ' ');
        }
        console.log('');
    }

    console.log('');
};

var _createMatrixScheme = function (N) {
    var matrix = [];

    for (var i = 0; i < N; i++) {
        matrix[i] = [];

        for (var j = 0; j < N; j++) {
            matrix[i][j] = [];
        }
    }

    return matrix;
};

var _createHorizontalMatrix = function (N) {
    var matrix = _createMatrixScheme(N), k = 1;

    for (var i = 0; i < N; i++) {
        for (var j = 0; j < N; j++, k++) {
            matrix[i][j] = k;
        }
    }

    return matrix;
};
"""
#####################################
"""
var _createMatrixScheme = function (N) {
    var matrix = [];

    for (var i = 0; i < N; i++) {
        matrix[i] = [];

        for (var j = 0; j < N; j++) {
            matrix[i][j] = [];
        }
    }

    return matrix;
};

suzdavam matrix = [],
dokato 'i' koeto e = 0 e po malko ot 5(primerno) da se 
pravi tova koeto e v skobite i sled vsqka iteraciq da se 
da se uvelichava s 1 dokato ne stigne 5(primerno)
matrix[i] = []
purvoto shte e matrix[0] = []
posle matrix[1] = [] i t.n.
posle za vsqko
matrix[0][j] = []
sushto e masiv toest imam 
0,
1,
2,
3,
4

pyrviq masiv koito e
0, [0, 1, 2, 3, 4]
1, [0, 1, 2, 3, 4]
2, [0, 1, 2, 3, 4]
3, [0, 1, 2, 3, 4]
4, [0, 1, 2, 3, 4]

Taka za vseki element ot purviq masiv slagam nov masiv 
ot 5(primerno) elementa

tova e kogato e zadaden index inache e prazen masiv
vse edno
[[],[],[],[],[]]
"""

#################################
"""
var _createHorizontalMatrix = function (N) {
    var matrix = _createMatrixScheme(N), k = 1;

    for (var i = 0; i < N; i++) {
        for (var j = 0; j < N; j++, k++) {
            matrix[i][j] = k;
        }
    }

    return matrix;
};

Posle puk s tazi funkciq mu kazvash:
vzemi edna prazna matrica => masiv ot prazni masivi
i zapochni da gi obrabotvash ot matrix[0][0] = 1
do matrix[4][4] = 25 vurtish cikula toest imash:
matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3
i t.n.
"""
########################################
"""
var _printMatrix = function (name, matrix) {
    console.log(name);

    for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < matrix[i].length; j++) {
            process.stdout.write(('000' + matrix[i][j]).slice(-2).toString() + ' ');
        }
        console.log('');
    }

    console.log('');
};


I sus printa printish vsichki koito sa ot 1 red 
toest ot matrix[0][0] od marix[0][4] na sushtiq red
led tova pochvash pak taka ot matrix[1][0] do matrix[1][4]
i taka do kraq. I tova se pravi sus vlojeni cikli kakto 
sum ti go napisal.
"""





































