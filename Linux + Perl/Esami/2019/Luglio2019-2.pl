#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>1);
my $par = shift or die $!;
my $nome=shift or die $!;
my @output =qx{lshw};
if($par=~/-s/)
{
    open(my $fh,">",$nome) or die $!;
    print $fh "@output";
    close $fh;
}
elsif($par=~/-b/)
{
    open(my $fh,"<",$nome) or die $!;
    my %hash;
    my %vendorDesc;
    my $vendor;
    while(<$fh>){
        if(m/(?i)vendor: (\N+)/)
        {
            $vendor=$1;
            $hash{$1}+=1;
        }
        $vendorDesc{$vendor}+="$1 \n$vendorDesc{$vendor}" if(m/\s+description:\s+(\N+)/);
    }

    foreach(sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys %hash )
    {print "$_ --> $hash{$_}\n";}

    foreach(sort{$a cmp $b} keys %vendorDesc)
    { print "$_ --> $vendorDesc{$_}\n";}

    close $fh;
}
else{die $!;}