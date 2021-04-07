#!/usr/bin/perl


##################              PASSO 1
# @parametri;
# push @parametri, shift or die $!;
# while(@ARGV)
# {
#     push @parametri, shift or die $!;    
# }
# $url = "'https://scholar.google.com/scholar?hl=en&q=";
# $str="$parametri[0]";
# for($i=1;$i<scalar @parametri;$i+=1)
# {
#     $str=$str."+$parametri[$i]";
# }

# @output=qx{wget -O output -U 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' $url$str'};

# @file = qx{cat output};
# for(@file)
# {
#     print "$1\n" if($_ =~ m/About (\S+) results/);
# }
# qx{rm output};



##################              PASSO 2
%hash;
$path= shift or die $!;
@file=qx{wget -O output.csv '$path'};
@apri=qx{cat output.csv};
foreach(@apri)
{
    $hash{$_}+=1;
}
@sorted=sort{$hash{$b}<=>$hash{$a} or $a cmp $b}keys %hash;
foreach(@sorted)
{
    print "$hash{$_} --> $_";
}
qx{rm output.csv};