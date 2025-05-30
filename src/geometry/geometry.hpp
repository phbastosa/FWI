# ifndef GEOMETRY_HPP
# define GEOMETRY_HPP

# include "../admin/admin.hpp"

class Geometry
{
public:

    int nsrc;
    int nrec;
    int nrel;

    int spread, nTraces;

    int * sInd = nullptr;
    int * iRec = nullptr;
    int * fRec = nullptr;

    float * xsrc = nullptr;
    float * zsrc = nullptr;

    float * xrec = nullptr;
    float * zrec = nullptr;

    std::string parameters;

    void set_parameters();     
};

# endif