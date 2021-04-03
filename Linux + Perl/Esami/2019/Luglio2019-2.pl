#!/usr/bin/perl
$par=shift or die $!;
$nomefile=shift or die $!;
@output=qx(lshw);
if($par =~m/-s/)
{
    open($fh,">",$nomefile) or die $!;
    print $fh @output;
    close $fh;
}
elsif($par =~m/-b/)
{
    open($fh,"<",$nomefile) or die $!;
    %hash;
    %descriptionVendor;
    while(<$fh>)
    {
        $desc;
        if(m/\s+description:\s(\N+)/)
        {
            $desc=$1;
        }

        if(m/\s+vendor\:\s+(\N+)/){
            $hash{$1}+=1;
            $descriptionVendor{$1}="$desc.\n$descriptionVendor{$1}";
        }
    }
    @sorted=sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys %hash;
    foreach(@sorted)
    {
        print "$_ --> $hash{$_}\n";
    }
    @sorted2=sort{$a cmp $b} keys %descriptionVendor;
    foreach(@sorted2)
    {
       print "$_ --> $descriptionVendor{$_}\n";
    }
    close $fh;
}
else{
    die $!;
}