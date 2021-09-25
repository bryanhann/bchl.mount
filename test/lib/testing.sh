#!/source/this/sh
_pass () { printf "\r[ ok ]\n" ; }
_fail () { printf "\r[fail]\n" ; }
_eq () {
    exp="$1"
    got="$2"
    [ "$exp" = "$got" ] && _pass && return 0
    _fail
    echo "          expected: $exp"
    echo "          received: $got"
    return 1
}
runtest () {
    printf "[----] $1" ;
    . $name
}
