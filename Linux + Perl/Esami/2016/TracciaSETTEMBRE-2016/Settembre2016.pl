#!/usr/bin/perl
@fantaSquadre=qx{cat ./fantaSquadre};
%puntiFantaSquadra;
$nomeSquadra;
foreach(@fantaSquadre)
{
    $nomeSquadra=$1 if(m/SQUADRA\:(\S+)/);
    if(m/FORMAZIONE:(\N+)/)
    {
        @splitted=split(",",$1);
        foreach(my $i=0;$i<scalar @splitted;$i++)
        {
            foreach(qx{ls ./pagelle | grep "giornata"})
            {
                foreach(qx{cat ./pagelle/$_})
                {
                    $puntiFantaSquadra{$nomeSquadra}+=$1 if(m/$splitted[$i]\-(\d+)/);
                }
            }
        }
    }
}
print "$_ --> $puntiFantaSquadra{$_}\n" foreach(keys %puntiFantaSquadra);