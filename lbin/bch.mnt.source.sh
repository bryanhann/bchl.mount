#!/bin/sh
bch_mnt_line4key  () { for line in $(bch.mnt.scan | grep  $1\=); do echo $line; done; }
bch_mnt_pair4line () { local IFS="="; echo $1 ;  }
bch_mnt_pair4key  () { echo $(bch_mnt_pair4line $(bch_mnt_line4key $1)) ; }
bch_mnt_val4pair  () { echo $2 ; }
bch_mnt_val4key   () { echo $(bch_mnt_val4pair $(bch_mnt_pair4key $1)) ; }
