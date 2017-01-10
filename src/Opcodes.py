class Opcodes():
    #
    # stack manipulation
    BPUSH   = b'0x00'
    SPUSH   = b'0x01'
    IPUSH   = b'0x02'
    FPUSH   = b'0x03'
    DPUSH   = b'0x04'
    SWAP    = b'0x05'
    SWAP2   = b'0x06'
    DUP     = b'0x07'
    DUP2    = b'0x08'

    # loading and storing variables
    BSTORE  = b'0x10'
    SSTORE  = b'0x11'
    ISTORE  = b'0x12'
    FSTORE  = b'0x13'
    DSTORE  = b'0x14'
    BLOAD   = b'0x15'
    SLOAD   = b'0x16'
    ILOAD   = b'0x17'
    FLOAD   = b'0x18'
    DLOAD   = b'0x19'

    # arithmetic and bitwise operations
    BADD    = b'0x20'
    BSUB    = b'0x21'
    BMUL    = b'0x22'
    BDIV    = b'0x23'
    BMOD    = b'0x24'
    BNOT    = b'0x25'
    BAND    = b'0x26'
    BOR     = b'0x27'
    BXOR    = b'0x28'
    SADD    = b'0x29'
    SSUB    = b'0x2A'
    SMUL    = b'0x2B'
    SDIV    = b'0x2C'
    SMOD    = b'0x2D'
    SNOT    = b'0x2E'
    SAND    = b'0x2F'
    SOR     = b'0x30'
    SXOR    = b'0x31'
    IADD    = b'0x32'
    ISUB    = b'0x33'
    IMUL    = b'0x34'
    IDIV    = b'0x35'
    IMOD    = b'0x36'
    INOT    = b'0x37'
    IAND    = b'0x38'
    IOR     = b'0x39'
    IXOR    = b'0x3A'
    FADD    = b'0x3B'
    FSUB    = b'0x3C'
    FMUL    = b'0x3D'
    FDIV    = b'0x3E'
    FMOD    = b'0x3F'
    FNOT    = b'0x40'
    FAND    = b'0x41'
    FOR     = b'0x42'
    FXOR    = b'0x43'
    DADD    = b'0x44'
    DSUB    = b'0x45'
    DMUL    = b'0x46'
    DDIV    = b'0x47'
    DMOD    = b'0x48'
    DNOT    = b'0x49'
    DAND    = b'0x4A'
    DOR     = b'0x4B'
    DXOR    = b'0x4C'

    # comparators
    #

    # logic and control flow
    GOTO    = b'0x50'
    JUMP    = b'0x51'
    IFE     = b'0x52'
    IFN     = b'0x53'
    IFNE    = b'0x54'
    IFLT    = b'0x55'
    IFLE    = b'0x56'
    IFGT    = b'0x57'
    IFGE    = b'0x58'

    # method invokation
    DEFINE  = b'0x80'
    INVOKE  = b'0x81'
    RETURN  = b'0x82'
    BRETURN = b'0x83'
    SRETURN = B'0x84'
    IRETURN = b'0x85'
    FRETURN = b'0x86'

    # type conversion
    #

    # system calls
    BPRINT  = b'0x90'
    SPRINT  = b'0x91'
    IPRINT  = b'0x92'
    FPRINT  = b'0x93'
    DPRINT  = b'0x94'
    APRINT  = b'0x95'
    BPROMPT = b'0x96'
    SPROMPT = b'0x97'
    IPROMPT = b'0x98'
    FPROMPT = b'0x99'
    DPROMPT = b'0x9A'
    APROMPT = b'0x9B'

    # do nothing
    PASS    = b'0xFF'